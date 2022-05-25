from django import forms
from jp_app.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'email',
            'role',
            'phone',
            'username',
            'password1',
            'password2',

        ]

class SignInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())