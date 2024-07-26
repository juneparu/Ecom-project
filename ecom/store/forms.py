# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from captcha.fields import CaptchaField

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     create_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ("username", "email", "create_password", "retype_password")
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#         }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    captcha = CaptchaField()