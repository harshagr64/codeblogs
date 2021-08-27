from django.urls import path
from . import views

urlspattern = [
    path("", views.index),
    path("posts", views.p),
    path("posts/<slug:slug>")
]