# Generated by Django 2.1.2 on 2018-10-08 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("blog", "0002_auto_20181008_1002")]

    operations = [
        migrations.RenameField(
            model_name="article", old_name="categorie", new_name="category"
        )
    ]
