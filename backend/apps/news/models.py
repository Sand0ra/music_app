from django.db import models


# Create your models here.

# Ваш код в models.py
class Photo(models.Model):
    image = models.ImageField('Фото новости', upload_to='news/')
    title = models.CharField('Заголовок', max_length=100, default='Default Title')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('Новость', max_length=100)
    public_date = models.DateTimeField('Дата выпуска новости', auto_now_add=True)
    description = models.TextField('описание новостей')
    photos = models.ManyToManyField(Photo, related_name='news_photos')
    slug = models.SlugField('Слаг', max_length=100, unique=True)
    image = models.ImageField('Обложка', upload_to='news/post')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-public_date']

    def __str__(self):
        return self.title
