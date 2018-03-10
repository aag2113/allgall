import collections

from six import itervalues
from elasticsearch_dsl import FacetedSearch, TermsFacet, DateHistogramFacet
from elasticsearch_dsl.query import Q

from .documents import PageHit


class PageHitSearch(FacetedSearch):
    doc_types = [PageHit]
    fields = ['fc_user_id', 'product_id']

    facets = collections.OrderedDict((
        ('is_known_article', TermsFacet(field='is_known_article')),
        ('is_known_product', TermsFacet(field='is_known_product')),
        ('doc_id', TermsFacet(field='doc_id')),
        ('user', TermsFacet(field='fc_user_id')),
        ('product', TermsFacet(field='product_id')),
        ('is_full', TermsFacet(field='is_full')),
        ('month', DateHistogramFacet(field='access_time', interval='month')),
    ))

    def search(self):
        s = super().search()
        s.aggs.bucket("top_articles", "terms", field="doc_id", size=100)
        return s

    def filter(self, search):
        filters = Q('match_all')
        for f in itervalues(self._filters):
            filters &= f
        return search.filter(filters)

    def query(self, search, query):
        """Overriden to use bool AND by default"""
        if query:
            return search.query(
                'multi_match',
                fields=self.fields,
                query=query,
                operator='and'
            ).sort('-Date')
        return search
