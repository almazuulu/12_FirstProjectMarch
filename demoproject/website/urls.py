from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),# www.adresswebsite.com/
    re_path("about_us", views.about_us, name='about_us'), #www.adresswebsite.com/about_us
    re_path("contact_us", views.contact_us, name='contact'),
]
