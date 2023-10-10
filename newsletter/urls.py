from django.urls import path, include, re_path

from .views import SubscribeView, ThankYouView, AlreadySubscribed
from . import views

app_name = 'newsletter'

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("thank_you/", ThankYouView.as_view(), name="thank_you"),
    path("already_subscribed/", AlreadySubscribed.as_view(),
         name="already_subscribed")
]
