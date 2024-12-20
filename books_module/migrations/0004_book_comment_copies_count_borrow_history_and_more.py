# Generated by Django 4.2 on 2024-12-06 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_module', '0003_book_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_comment',
            name='copies_count',
            field=models.PositiveIntegerField(default=0, verbose_name='how many copies of this book are available'),
        ),
        migrations.CreateModel(
            name='Borrow_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_users', to='books_module.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='borrow_history',
            constraint=models.UniqueConstraint(fields=('user', 'borrowed_book'), name='make sure each user can only borrowed one copy of each book'),
        ),
    ]
