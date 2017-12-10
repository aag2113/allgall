from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
import json
import datetime
import smtplib
import os
from email.mime.text import MIMEText

class TrialFormView(generic.base.TemplateView):
    template_name = 'freepreview/trialform.html'

class submissionSuccessView(generic.base.TemplateView):
    template_name = 'freepreview/success.html'

def TrialFormSubmit(request):
    qd = request.POST
    
    sender = 'adam@factcite.com'
    recipient = 'adam@factcite.com'
    recipient2 = 'owls@factcite.com'
    u,p = open(os.path.join(os.path.dirname(__file__),'pw.conf'),'rb').readline().strip().split(',')

    emailTxt = ''
    emailTxt += 'Name: ' + qd.get('name') + '\n'
    emailTxt += 'Position: ' + qd.get('position') + '\n'
    emailTxt += 'State: ' + qd.get('state') + '\n'
    emailTxt += 'Institution: ' + qd.get('institution') + '\n'
    emailTxt += 'Email: ' + qd.get('email') + '\n'
    emailTxt += 'Phone: ' + qd.get('phone') + '\n'
    emailTxt += 'Username: ' + qd.get('username') + '\n'
    emailTxt += 'Password: ' + qd.get('password') + '\n'

    msg = MIMEText(emailTxt)

    msg['Subject'] = 'FactCite Trial Request'
    msg['From'] = sender
    msg['To'] = recipient

    s = smtplib.SMTP('smtp.office365.com',587)
    s.ehlo()
    s.starttls()
    s.login(u,p)
    s.sendmail(sender, [recipient], msg.as_string())
    s.sendmail(sender, [recipient2], msg.as_string())
    s.quit()

    return HttpResponseRedirect('/freepreview/success/')
