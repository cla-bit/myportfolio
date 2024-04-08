from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_contact_email(contact):
    # Email the sender
    template_sender = render_to_string('base/email_sending.html', {'Name': contact.name, 'Email': contact.email})
    email_sender = EmailMessage(
        'Message Notification',
        template_sender,
        settings.EMAIL_HOST_USER,
        [contact.email],
    )
    email_sender.send(fail_silently=False)

    # Email the receiver (you can customize this part)
    # Assuming you have a "receiver_email" variable set to the receiver's email address
    template_receiver = render_to_string('base/email_receiving.html', {
        'Name': contact.name, 'Email': contact.email, 'Subject': contact.subject, 'Message': contact.message})
    email_receiver = EmailMessage(
        'Message Notification',
        template_receiver,
        settings.EMAIL_HOST_USER,
        [settings.RECEIVER_EMAIL],
    )
    email_receiver.send(fail_silently=False)
