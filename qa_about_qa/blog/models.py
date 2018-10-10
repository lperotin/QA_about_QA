from django.db import models
from django.contrib import admin
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(
        default=timezone.now, verbose_name="date of publication"
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "blog post"
        ordering = ["date"]

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
