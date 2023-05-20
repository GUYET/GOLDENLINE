from django.urls import path
from . import views

urlpatterns = [
    path("visualisation/", views.visualisation),
]
