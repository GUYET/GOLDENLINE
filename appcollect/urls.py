from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("visualisation/", views.visualisation),
    path("login/", views.visualisation),
]
