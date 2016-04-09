from django.views import generic
from accounts.forms import UserForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# ToDo: find more elegant way to create a TaskList upon user registration
from ToDo.models import TaskList, Task

# Create your views here.

class accountsView(generic.base.TemplateView):
	template_name = 'accounts/base.html'

def register(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user.set_password(new_user.password)
			new_user.save()
			messages.info(request, "Thank you for registering!")
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password'],
									)
			# Give the new user a tasklist so they don't redirect to an empty page
			# TODO: This probably should not live here
			tl = TaskList.objects.create(owner=new_user, title='Tasks')
			Task.objects.create(taskList = tl, title='Register for AllGall', status=1)
			Task.objects.create(taskList = tl, title='Go get it!')
			login(request, new_user)
			return HttpResponseRedirect('/ToDo/')
		else:
			print form.errors
	else:
		form = UserForm()

	return render(request, 'accounts/register.html', {'form':form})