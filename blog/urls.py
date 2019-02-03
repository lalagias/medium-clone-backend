"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('groups/', views.GroupList.as_view(), name="group-list"),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name="group-detail"),
    path('profiles/', views.ProfileList.as_view(), name="profile-list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile-detail"),
    path('posts/', views.PostList.as_view(), name="post-list"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
    path('comments/', views.CommentList.as_view(), name="comment-list"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name="comment-detail"),
]
