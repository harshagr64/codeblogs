from django.urls import path
from . import views

urlspattern = [
    path("", views.starting_page, name = ""),
    path("posts", views.posts),
    path("posts/<slug:slug>", views.post_detail)
]
