# Generated by Django 4.2.7 on 2023-12-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Фото новости')),
                ('title', models.CharField(default='Default Title', max_length=100, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Новость')),
                ('public_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска новости')),
                ('description', models.TextField(verbose_name='описание новостей')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(upload_to='news/post', verbose_name='Обложка')),
                ('photos', models.ManyToManyField(related_name='news_photos', to='news.photo')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-public_date'],
            },
        ),
    ]
