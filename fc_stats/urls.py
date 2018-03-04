from django.conf.urls import url

from .views import UsageVisualizerView, FcUserAutocomplete

app_name = "usage"
urlpatterns = [
    url(r'^$', UsageVisualizerView.as_view(), name='usage_visualizer'),
    url(
        r'^autocomplete/fcuser/$',
        FcUserAutocomplete.as_view(),
        name='fcuser_autocomplete'
    )
]