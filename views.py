from django.views import generic

# Create your views here.

class accountsView(generic.base.TemplateView):
	template_name = 'accounts\\base.html'