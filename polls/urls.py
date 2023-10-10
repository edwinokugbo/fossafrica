from django.urls import path, re_path

# from .views import DashboardListView
from . import views

app_name = 'polls'

urlpatterns = [
    re_path(r'^$', views.index, name='polls_page'),
    path('poll_choices/<str:pk>/',
         views.pollChoices, name='poll_choices'),
    path('vote_now/<str:pk>/',
         views.voteNow, name='vote_now'),
    path('add_poll/', views.addPoll, name="add_poll"),
    path('edit_poll/<str:pk>/', views.editPoll, name="edit_poll"),
    path('del_poll/<str:pk>/', views.delPoll, name="del_poll"),

    path('add_choice/<str:pk>', views.addChoice, name="add_choice"),
    path('edit_choice/<str:pk>/', views.editChoice, name="edit_choice"),
    path('del_choice/<str:pk>/', views.delChoice, name="del_choice"),
]
