# Generated by Django 4.2 on 2024-11-24 09:16

import books_module.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0002_book_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_comment',
            name='rating',
            field=models.IntegerField(default=0, validators=[books_module.models.rating_validator], verbose_name='rating of this book'),
        ),
    ]
