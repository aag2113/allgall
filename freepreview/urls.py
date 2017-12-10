from django.conf.urls import url

from .views import TrialFormView, TrialFormSubmit, submissionSuccessView

app_name = 'freepreview'
urlpatterns = [
	# /freepreview/
	url(r'^$', TrialFormView.as_view(), name='index'),
	# /freepreview/submit/
	url(r'^submit/$', TrialFormSubmit, name='submitForm'),
	# /freepreview/success/
	url(r'^success/$', submissionSuccessView.as_view(), name='success'),
]
