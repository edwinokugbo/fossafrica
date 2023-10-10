from django.urls import path, include, re_path

from .views import HomePageView
from . import views

app_name = 'blog'

urlpatterns = [

    # re_path('blog/', views.blog, name='blog'),
    re_path(r'^$', views.Blog.as_view(), name='blog'),
    path('post/<int:post_id>/<str:post_title>/', views.post, name='post'),
    path('addpost/', views.addPost, name="addpost"),
    path('editpost/<str:pk>/', views.editPost, name="editpost"),
    path('delpost/<str:pk>/', views.delPost, name="delpost"),
    path('postcomment/<str:pk>/', views.postComment, name="postcomment"),
]
