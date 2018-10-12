from django.contrib import admin
from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display = ("title", "category", "author", "date")
    list_filter = ("author", "category")
    date_hierarchy = "date"
    ordering = ("date",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        (
            "General",
            {
                "classes": ["collapse"],
                "fields": ("title", "author", "category", "slug"),
            },
        ),
        # Fieldset 2 : contenu de l'article
        (
            "Article content",
            {
                "description": "The form accepts HTML",
                "fields": ("content", "picture"),
            },
        ),
    )

    # Colonnes personnalisées
    def view_content(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut rajouter des points de suspension.
        """
        text = article.content[0:40]
        if len(article.content) > 40:
            return "%s…" % text
        else:
            return text

    view_content.short_description = "Content view"


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
