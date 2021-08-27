from django.urls import path
from . import view

urlspattern = [
    path("", views.index),
    path("posts"),
    path("posts/<slug:slug>")
]