from smtplib import SMTP
from email.mime.text import MIMEText

from django.conf import settings


def send_mail(subject, message, recipients):
    sender = settings.EMAIL_USER
    sender_pw = settings.EMAIL_PASSWORD
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    recipients = recipients.split(",")

    s = SMTP(settings.EMAIL_SERVER, settings.EMAIL_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, sender_pw)
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
