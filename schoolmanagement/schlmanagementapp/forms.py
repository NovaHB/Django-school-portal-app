
from django import forms
from django.core import validators #importing the validator class
from django.core.exceptions import ValidationError

from django.forms import ModelForm, Textarea, TextInput,PasswordInput
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class LoginPage(forms.Form):
    email=forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'id': 'username', "placeholder":"Username"}))
    password=forms.CharField(label="Password", max_length=15, widget=forms.TextInput(attrs={'id': 'passkey', "placeholder":"Password"}))