from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("article/<slug:slug>", views.view_article, name="view_article"),
    path("contact", views.contact, name="contact"),
]
