from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'FirstName'
        }
    ))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'LastName'
        }
    ))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class MySignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request):
        user = super(SignupForm, self).save(request)
        user.first_name = self.cleaned_data('first_name')
        user.last_name = self.cleaned_data('last_name')
        user.save()
