from django.shortcuts import render
from django.views import generic

from.models import BlogPost


class HomePageView(generic.base.TemplateView):
    template = 'adam/index.html'

    def get(self, request):
        posts = BlogPost.objects.filter(date_published__isnull=False).order_by('-date_published')
        return render(request, self.template, {'blogposts': posts})
