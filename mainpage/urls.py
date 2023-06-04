from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from mainpage import views

urlpatterns = [
    path('', views.index, name='index'),
]
