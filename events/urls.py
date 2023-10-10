from django.urls import path, include, re_path

from . import views

app_name = 'events'

urlpatterns = [

    re_path(r'^$', views.Events.as_view(), name='events'),
    path('add_event/', views.addEvent, name="add_event"),
    path('edit_event/<str:pk>/', views.editEvent, name="edit_event"),
    path('del_event/<str:pk>/', views.delEvent, name="del_event"),
    path('event/<int:event_id>/<str:event_title>/', views.event, name='event'),
    path("subscribe/", views.SubscribeView.as_view(), name="subscribe"),
    path("thank_you/", views.ThankYouView.as_view(), name="thank_you"),
    path("already_subscribed/", views.AlreadySubscribed.as_view(),
         name="already_subscribed")]
