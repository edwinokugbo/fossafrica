from dataclasses import field
from email.policy import default
from random import choices
from django import forms
from .models import Question, Choice
from django.contrib.admin.widgets import AdminSplitDateTime

from django_summernote.widgets import SummernoteWidget, SummernoteWidgetBase


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date', 'privacy',
                  'authorized_participants', 'show_result', 'poll_status']
        widgets = {
            'pub_date': forms.SelectDateWidget()
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'description',
                  'choice_img']
