# Generated by Django 4.2.1 on 2023-05-13 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="address",
        ),
        migrations.RemoveField(
            model_name="category",
            name="author",
        ),
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
        migrations.RemoveField(
            model_name="category",
            name="is_published",
        ),
        migrations.RemoveField(
            model_name="category",
            name="price",
        ),
    ]
