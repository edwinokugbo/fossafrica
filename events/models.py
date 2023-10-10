from email.policy import default
from email.utils import localtime
from pydoc import describe
from tkinter import CASCADE
from django.db import models
from django.conf import settings


class Event(models.Model):
    EVENT_STATUS_CH = ((0, 'Draft'), (1, 'Published'), (2, 'Archive'))
    APPROVE_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Suspended'))
    PRIVACY_CHOICES = ((0, 'Private'), (1, 'Public'), (2, 'Group'))
    LOCATION_CHOICES = ((1, 'Offline'), (2, 'Online'))
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    featured_img = models.ImageField(upload_to='events/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speakers = models.TextField(null=True)
    participants = models.TextField(null=True)
    privacy = models.IntegerField(null=True, choices=PRIVACY_CHOICES)
    date_created = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    anchor = models.CharField(max_length=100, null=True)
    location = models.IntegerField(default=1, choices=LOCATION_CHOICES)
    location_name = models.CharField(max_length=255, null=True)
    event_status = models.IntegerField(default=0, choices=EVENT_STATUS_CH)
    approval = models.IntegerField(
        default=0, null=True, choices=APPROVE_STATUS)

    def __str__(self):
        return self.title


class Journal(models.Model):
    APPROVE_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Suspended'))
    title = models.CharField(max_length=100)
    note = models.TextField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    journal_status = models.IntegerField(choices=APPROVE_STATUS, default=1)


class Participant(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=120)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_status = models.IntegerField(default=1)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
