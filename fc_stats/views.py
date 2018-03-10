import urllib
from dal import autocomplete
from datetime import datetime

from django.views import generic
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import FcUser, Product, Article

from .connections import connections
from .forms import UsageStatsForm
from .searches import PageHitSearch


class FcUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = FcUser.objects.all()

        if self.q:
            qs = qs.filter(username__startswith=self.q)

        return qs

class UsageVisualizerView(generic.base.TemplateView):
    template_name = "usage/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def convert_facet_value(self, facet_name, value):
        if facet_name == 'user':
            try:
                return FcUser.objects.get(pk=value).username
            except ObjectDoesNotExist:
                return "{}*".format(value)
        elif facet_name == 'product':
            try:
                return Product.objects.get(pk=value).product_key
            except ObjectDoesNotExist:
                return "{}*".format(value)
        elif facet_name == 'doc_id':
            try:
                return Article.objects.get(pk=value).__str__()
            except ObjectDoesNotExist:
                return "{}*".format(value)
        elif facet_name == 'month':
            return value.strftime('%Y-%m')

        return value

    def href_with_removed(self, key, request, value):
        existing = dict(request.GET.items())
        for key, value in existing.items():
            existing[key] = value
        if key in existing:
            del existing[key]
        return './?' + urllib.parse.urlencode(existing)

    def href_with_added(self, key, request, value):
        existing = dict(request.GET.items())
        existing[key] = value
        for key, value in existing.items():
            existing[key] = value
        return './?' + urllib.parse.urlencode(existing)

    def facet_to_filter(self, facet_name, value):
        boolean_facets = ['is_known_article', 'is_known_product', 'is_full']
        numerical_facets = ['doc_id', 'user', 'product']

        if facet_name == 'month':
            yyyy, mm = map(int, value.split('-'))
            return datetime.datetime(yyyy, mm, 1, 0, 0, 0)
        elif facet_name in boolean_facets:
            return value
        elif facet_name in numerical_facets:
            return int(value)

        return value

    def get(self, request, **kwargs):
        if request.GET:
            form = UsageStatsForm(request.GET)
        else:
            form = UsageStatsForm(initial={"is_known_article": True, "is_known_product": True})

        whitelisted_facet_args = {}
        if not request.GET:
            whitelisted_facet_args['is_known_article'] = True
            whitelisted_facet_args['is_known_product'] = True
        for key, value in request.GET.items():
            if key in PageHitSearch.facets and value:
                if key in ['is_known_article', 'is_known_product']:
                    if not value:
                        value = True
                    else:
                        value = value == 'on'
                whitelisted_facet_args[key] = self.facet_to_filter(key, value)

        query = None

        s = PageHitSearch(query=query, filters=whitelisted_facet_args)
        response = s.execute()
        facets = response.facets
        facets = [(k, v) for k, v in facets._d_.items()]
        facet_dicts = []
        for facet_name, values in facets:
            facet_values = []
            for value, count, selected in values:
                display_value = self.convert_facet_value(facet_name, value)
                if selected:
                    href = self.href_with_removed(facet_name, request, value)
                else:
                    href = self.href_with_added(facet_name, request, value)
                facet_values.append({
                    'value': value,
                    'display_value': display_value,
                    'count': count,
                    'selected': selected,
                    'href': href,
                })
            facet_dict = {
                'name': facet_name,
                'vals': facet_values
            }
            facet_dicts.append(facet_dict)

        total = response.hits.total

        top_hits = []
        for hit in response.to_dict().get('aggregations').get('top_articles').get('buckets'):
            a = Article.objects.get(id=hit.get('key'))
            hit["title"] = a.title
            hit["product"] = a.product
            top_hits.append(hit)

        ctx = {
            'total': total,
            'form': form,
            'facets': facet_dicts,
            'docs': list(response),
            'hits': top_hits,
        }
        return render(request, 'usage/base.html', context=ctx)
