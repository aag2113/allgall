from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
import json
import datetime

class HomePageView(generic.base.TemplateView):
    template_name = 'adam/index.html'

