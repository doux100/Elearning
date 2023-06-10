from django.shortcuts import render
from .models import Data
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def contact(request):
    mydata = Data.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            f'\"{name}\" has send you the message below: \n{message}\nSender Email is : {email}',
            email,
            [settings.EMAIL_HOST_USER],
        )
    cont = {'mydata': mydata}
    return render(request, 'contact.html', cont)
