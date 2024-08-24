# Generated by Django 5.0.6 on 2024-08-20 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.PositiveSmallIntegerField()),
                ('cover_photo', models.ImageField(upload_to='book_covers/')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultUserProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='flashcards_profile_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='blog_videos/')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('body', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserBookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WebImgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('thumbnail', models.ImageField(upload_to='web_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=5000)),
                ('page_photo', models.ImageField(upload_to='book_pages/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='ilovecookbooks.book')),
            ],
        ),
    ]
