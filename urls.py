from django.conf.urls import patterns, url
from accounts import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	# Accounts 
    url(r'^$', login_required(views.accountsView.as_view()), name='accounts'),

    # Login
    # Next Page behavior for login 
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'template_name': 'accounts/login.html'}),
    
    # Logout
    url(r'^logout/$','django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/accounts/login'}),

    # Register
    url(r'^register/$', views.register, name='register'),
)