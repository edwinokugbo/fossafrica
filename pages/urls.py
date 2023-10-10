from django.urls import path, include, re_path

from .views import DashboardListView, SignupPageView
from . import views

app_name = 'pages'

urlpatterns = [
    # path('about/', HomePageView.as_view(), name='home'),
    re_path(r'^$', views.index, name='index'),
    re_path('about/', views.About.as_view(), name='about'),
    re_path('contact/', views.Contact.as_view(), name='contact'),
    re_path('news/', views.News.as_view(), name='news'),
    re_path('login/', views.loginPage, name="login"),   
    re_path('logout/', views.logoutPage, name="logout"),
    re_path('signup/', SignupPageView.as_view(), name="home"),
    path("home/", DashboardListView.as_view(), name="home")

]
