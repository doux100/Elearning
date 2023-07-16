from captcha.fields import ReCaptchaField
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()
