from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,reciever):
    #Creating message subject and sender
    subject = 'Welcome to the Accolades'
    sender = 'lingxing0549@gmail.com'

    #passing in context variables
    text_content = render_to_string('email/awardsemail.txt',{"name":name})
    html_content = render_to_string('email/awardsemail.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[reciever])
    msg.attach_alternative(html_content,text/html)
    msg.send()