from dataclasses import field, fields
from email.policy import default
from random import choices
from django import forms
from .models import Comment, Post
from django.contrib.admin.widgets import AdminSplitDateTime

from django_summernote.widgets import SummernoteWidget, SummernoteWidgetBase


class PostForm(forms.ModelForm):
    """Form for blog post"""
    class Meta:
        model = Post
        fields = [
            'Title', 'Subtitle', 'Content', 'category', 'Author', 'DateCreated', 'PostTags', 'FeatureImage', 'PostStatus']
        widgets = {
            'Content': SummernoteWidget(),
            'DateCreated': forms.SelectDateWidget()
        }


class FeatureImageForm(forms.ModelForm):
    """Form for uploading feature image"""
    class Meta:
        model = Post
        fields = ('FeatureImage',)


class CommentForm(forms.ModelForm):
    """Form to post comment"""

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_text'].label = 'Enter Comment'

    class Meta:
        model = Comment
        fields = ['author', 'comment_text']
