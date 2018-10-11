from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category

# TODO find how not to set this variable in each view
categories = Category.objects.all()

def home(request):
    articles = Article.objects.all()
    return render(request, "blog/home.html", {"last_articles": articles, "categories": categories})

def view_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/view_article.html", {"article": article, "categories": categories})

def view_articles_by_category(request, category_name):
    articles_from_category = Article.objects.filter(category__name__contains=category_name)
    return render(request, "blog/view_articles_by_category.html", {"articles_from_category": articles_from_category, "categories": categories})

def contact(request):
    return render(request, "blog/contact.html", {"categories": categories})

