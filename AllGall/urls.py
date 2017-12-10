from django.conf.urls import include, url
from django.contrib import admin

from accounts import urls as accounts_urls
from freepreview import urls as freepreview_urls
from ToDo import urls as todo_urls

from adam.views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^ToDo/', include(todo_urls, namespace='ToDo')),
    url(r'^freepreview/', include(freepreview_urls, namespace='freepreview')),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
]
