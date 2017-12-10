from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import (taskView, createTask, check, updateTitle, TLupdateTitle, createTaskList, toggleTaskList,
                    removeTaskList, saveWidgetPos, clearCompleted, updateOrder, taskListView, saveWidgetSize)

app_name = 'ToDo'
urlpatterns = [
    # /ToDo/
    url(r'^$', login_required(TemplateView.as_view(template_name='ToDo/index.html')), name='index'),

    # /ToDo/task/5/
    url(r'^task/(?P<pk>\d+)/$', login_required(taskView.as_view()), name='task'),

    # /ToDo/task/create/
    url(r'^task/create/$', createTask, name='createTask'),

    # /ToDo/task/5/check/
    url(r'^task/(?P<task_id>\d+)/check/$', check, name='check'),

    # /ToDo/task/5/updateTitle/
    url(r'^task/(?P<task_id>\d+)/updateTitle/$', updateTitle, name='updateTitle'),

    # /ToDo/taskList/5/updateTitle/
    url(r'^taskList/(?P<tasklist_id>\d+)/updateTitle/$', TLupdateTitle, name='TLupdateTitle'),

    # /ToDo/tasklist/1/
    url(r'^tasklist/(?P<pk>\d+)/$', login_required(taskListView.as_view()), name='tasklist'),

    # /ToDo/tasklist/create/
    url(r'^tasklist/create/$', createTaskList, name='createTaskList'),

    # /ToDo/tasklist/1/toggle/
    url(r'^tasklist/(?P<tasklist_id>\d+)/toggle/$', toggleTaskList, name='toggleTaskList'),

    # /ToDo/tasklist/5/remove/
    url(r'^tasklist/(?P<tasklist_id>\d+)/remove/$', removeTaskList, name='removeTaskList'),

    # /ToDo/tasklist/5/saveWidgetSize/
    url(r'^tasklist/(?P<tasklist_id>\d+)/saveWidgetSize/$', saveWidgetSize, name='saveWidgetSize'),

    # /ToDo/tasklist/5/saveWidgetPos/
    url(r'^tasklist/(?P<tasklist_id>\d+)/saveWidgetPos/$', saveWidgetPos, name='saveWidgetPos'),

    # /ToDo/tasklist/5/clearCompleted/
    url(r'^tasklist/(?P<tasklist_id>\d+)/clearCompleted/$', clearCompleted, name='clearCompleted'),

    # /ToDo/tasklist/5/updateOrder/
    url(r'^tasklist/(?P<tasklist_id>\d+)/updateOrder/$', updateOrder, name='updateOrder'),
]
