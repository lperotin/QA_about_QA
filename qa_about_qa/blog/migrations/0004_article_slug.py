# Generated by Django 2.1.2 on 2018-10-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0003_auto_20181008_1002")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="slug",
            field=models.SlugField(default="default_slug", max_length=100),
        )
    ]
