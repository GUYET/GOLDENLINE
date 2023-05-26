from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("visualisation/", views.visualisation),
    path("accounts/", include("django.contrib.auth.urls")),
]
