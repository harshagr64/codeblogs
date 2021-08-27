from django.urls import path
from .

urlspattern = [
    path("", views.index),
    path("posts"),
    path("posts/<slug:slug>")
]