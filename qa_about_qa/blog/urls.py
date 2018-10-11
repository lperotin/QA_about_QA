from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<str:category_name>", views.view_articles_by_category, name="view_articles_by_category"),
    path("article/<slug:slug>", views.view_article, name="view_article"),
    path("contact", views.contact, name="contact"),
]
