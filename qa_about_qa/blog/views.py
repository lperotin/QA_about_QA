from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, "blog/home.html", {"last_articles": articles})


# def lire(request, slug):
#     article = get_object_or_404(Article, slug=slug)
#     return render(request, "blog/lire.html", {"article": article})


def view_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/view_article.html", {"article": article})

def contact(request):
    return render(request, "blog/contact.html")

