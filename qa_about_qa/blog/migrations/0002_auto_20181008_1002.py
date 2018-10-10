# Generated by Django 2.1.2 on 2018-10-08 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("blog", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="categorie",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.Category",
            ),
            preserve_default=False,
        ),
    ]
