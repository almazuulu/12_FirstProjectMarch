from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.listnews, name='blog'), # www.example.com/blog/
    path('singlenews/', views.singleblog, name='singlenews'), #www.example.com/blog/singlenews/
]
