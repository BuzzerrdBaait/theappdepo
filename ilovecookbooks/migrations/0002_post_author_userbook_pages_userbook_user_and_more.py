# Generated by Django 5.0.6 on 2024-08-24 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilovecookbooks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userbook',
            name='pages',
            field=models.ManyToManyField(through='ilovecookbooks.UserBookPage', to='ilovecookbooks.bookpage'),
        ),
        migrations.AddField(
            model_name='userbook',
            name='user',
            field=models.ForeignKey(default='unkown', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userbookpage',
            name='book_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ilovecookbooks.bookpage'),
        ),
        migrations.AddField(
            model_name='userbookpage',
            name='user_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ilovecookbooks.userbook'),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='title',
            field=models.CharField(default='idk', max_length=200),
        ),
    ]
