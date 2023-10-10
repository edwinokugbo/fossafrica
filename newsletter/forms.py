from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    """ Form for front page footer subscription feature """

    class Meta:
        model = Subscriber
        fields = ['email']
