from django import forms
from django.contrib.auth.models import User
from .models import Profile
from datetime import date
from django.core.exceptions import ValidationError



class DateInput(forms.DateInput):
    input_type = 'date'


def dob_validator(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of birth cannot be in the future.')

"""class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']"""

class ProfileForm(forms.ModelForm):
    dob = forms.DateField(widget = DateInput(), validators=[dob_validator])

    class Meta:
        model = Profile
        exclude = ['user']