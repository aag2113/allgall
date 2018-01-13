from django.http import HttpResponseRedirect
from django.views import generic

from AllGall.utilities import send_mail


class TrialFormView(generic.base.TemplateView):
    template_name = 'freepreview/trialform.html'


class submissionSuccessView(generic.base.TemplateView):
    template_name = 'freepreview/success.html'


def TrialFormSubmit(request):
    qd = request.POST

    subject = "Factcite Trial Request"
    recipients = 'adam@factcite.com, owls@factcite.com'

    emailTxt = ''
    emailTxt += 'Name: ' + qd.get('name') + '\n'
    emailTxt += 'Position: ' + qd.get('position') + '\n'
    emailTxt += 'State: ' + qd.get('state') + '\n'
    emailTxt += 'Institution: ' + qd.get('institution') + '\n'
    emailTxt += 'Email: ' + qd.get('email') + '\n'
    emailTxt += 'Phone: ' + qd.get('phone') + '\n'
    emailTxt += 'Username: ' + qd.get('username') + '\n'
    emailTxt += 'Password: ' + qd.get('password') + '\n'

    send_mail(subject, emailTxt, recipients)

    return HttpResponseRedirect('/freepreview/success/')
