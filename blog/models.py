from unicodedata import category
from django.conf import settings
from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    POST_STATUS = ((0, 'Draft'), (1, 'Published'), (2, 'Archive'))
    APPROVE_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Suspended'))
    Title = models.CharField(max_length=255)
    Subtitle = models.CharField(max_length=255, default="", blank=True)
    Content = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    Author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    DateCreated = models.DateTimeField(default=datetime.now, null=True)
    PostTags = models.TextField(null=True)
    DateModified = models.DateTimeField(auto_now=True)
    FeatureImage = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)
    PostStatus = models.IntegerField(default=0, choices=POST_STATUS)
    Approval = models.IntegerField(
        default=0, null=True, choices=APPROVE_STATUS)
    reaction = models.IntegerField(null=True)

    def __str__(self):
        return self.Title

    def get_record(self):
        return self.objects.get()


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    DatePosted = models.DateTimeField(auto_now=True)
    DateModified = models.DateTimeField(auto_now=True)
    reply_to = models.IntegerField(null=True)
    reaction = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.comment_text
