from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import News


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'news'
    queryset = News.objects.all()


class NewsView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.all()

class NewsDetailView(DetailView):
    model = News  # обьединяем модел с таблицой Музикu из базы данных
    template_name = 'news_detail.html'  # обьединяем html code
    context_object_name = 'news'  # даем имя что бы обращатся к базе
    queryset = News.objects.all()  # вытаскием все модели не все группы а именно модели
