from django.conf.urls import url

from .views import HomePageView

app_name = 'adam'
urls = [
    # /adam/
    url(r'^index/$', HomePageView.as_view(), name='adam_index'),
]
