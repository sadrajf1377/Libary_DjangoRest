# Generated by Django 4.2 on 2024-10-05 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='title of category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='title of this book')),
                ('author', models.CharField(max_length=30, verbose_name='who wrote this book')),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=8)),
                ('publish_date', models.DateField(verbose_name='date of publishment')),
                ('book_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books_module.book_category')),
            ],
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='check replication'),
        ),
    ]
