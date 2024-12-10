# Generated by Django 4.2 on 2024-11-23 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='time of comment creation')),
                ('content', models.TextField(max_length=2000, verbose_name='main content of comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='writter of comment')),
                ('parent_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books_module.book')),
            ],
        ),
    ]
