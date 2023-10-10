from django.conf import settings
from django.db import models
from datetime import datetime


class Question(models.Model):
    POLL_STATUS = ((0, 'Draft'), (1, 'Published'),
                   (2, 'Ended'), (3, 'Suspended'), (4, 'Cancelled'))
    APPROVAL_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Suspended'))
    PRIVACY_CHOICES = ((1, 'Members'), (2, 'Public'), (3, 'Group'))
    SHOW_RESULT = ((0, 'Show Result'), (1, 'Hide Result'))

    question_text = models.CharField(max_length=200)
    poll_category = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField(
        default=datetime.now, help_text='date published')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    privacy = models.IntegerField(choices=PRIVACY_CHOICES, default=2)
    authorized_participants = models.TextField(blank=True)
    show_result = models.IntegerField(choices=SHOW_RESULT, default=0)
    poll_status = models.IntegerField(choices=POLL_STATUS, default=0)
    approval_status = models.IntegerField(choices=APPROVAL_STATUS, default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    choice_img = models.ImageField(upload_to='polls/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    vote_date = models.DateTimeField('date voted')

    def __str__(self):
        return self.question.question_text + " > " + self.choice.choice_text
