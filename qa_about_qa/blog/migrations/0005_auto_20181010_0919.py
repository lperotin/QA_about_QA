# Generated by Django 2.1.2 on 2018-10-10 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date'], 'verbose_name': 'blog post'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='auteur',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='contenu',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='titre',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nom',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date of publication'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
