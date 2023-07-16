from django.shortcuts import render
from .forms import ContactForm
from .models import Data
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def contact(request):
    mydata = Data.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            def get_data(y):
                return form.cleaned_data[y]
            send_mail(
                get_data('subject'),
                f'\"{get_data("name")}\" has send you the message below: \n{get_data("message")}\nSender Email is : {get_data("email")}',
                get_data("email"),
                [settings.EMAIL_HOST_USER],
            )
    else:
        form = ContactForm()
    cont = {'mydata': mydata, 'form': form}
    return render(request, 'contact.html', cont)
