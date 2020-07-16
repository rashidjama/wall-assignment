"""wall_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from login import views as login_views
from blog_app import views as blog_app_views

urlpatterns = [
    path('', login_views.index),
    path('success', login_views.success),
    path('register', login_views.register),
    path('login', login_views.login),
    path('logout', login_views.logout),
    path('wall', blog_app_views.wall),
    path('create_message', blog_app_views.create_message),
    path('create_comment/<int:post_id>', blog_app_views.create_comment),
    path('<int:user_id>/delete_user', blog_app_views.delete, name='remove'),
    path('<int:post_id>/delete_post', blog_app_views.delete_post, name='delete_post')
]
