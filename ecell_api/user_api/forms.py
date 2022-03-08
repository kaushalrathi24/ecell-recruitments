import email
from unicodedata import name
from django import forms


class NewForm(forms.Form):
    _id = forms.CharField(max_length=25)
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    role = forms.CharField(max_length=25)
    active = forms.BooleanField()
    password = forms.CharField(widget=forms.PasswordInput())

class UpdateForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    role = forms.CharField(max_length=25)
    active = forms.BooleanField()