import email
from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=((0, 'Unsubscribed'), (1, 'Subscribed')), default=1)

    def __str__(self):
        return self.email
