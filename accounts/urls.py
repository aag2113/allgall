from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from .views import accountsView, register


app_name = 'accounts'
urlpatterns = [
	# Accounts 
    url(r'^$', login_required(accountsView.as_view()), name='accounts'),

    # Login
    # Next Page behavior for login 
    url(r'^login/$', login, name='login', kwargs={'template_name': 'accounts/login.html'}),
    
    # Logout
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/accounts/login'}),

    # Register
    url(r'^register/$', register, name='register'),
]