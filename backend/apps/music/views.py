from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Singer, Group, Music


# Create your views here.


class SingersView(ListView):
    model = Singer
    template_name = 'singers.html'
    context_object_name = 'singers'
    queryset = Singer.objects.all()


class GroupsView(ListView):
    model = Group
    template_name = 'groups.html'
    context_object_name = 'groups'  # object list
    queryset = Group.objects.all()


class GroupsDetailView(DetailView):
    model = Group
    template_name = 'groups_details.html'
    context_object_name = 'group'  # object list
    queryset = Group.objects.all()


class SingerDetailView(DetailView):
    model = Singer
    template_name = 'singers_detail.html'
    context_object_name = 'singer'  # object list
    queryset = Singer.objects.all()


class MusicListView(ListView):
    model = Music
    template_name = 'music_list.html'
    context_object_name = 'musics'
    queryset = Music.objects.all()


class MusicDetailView(DetailView):
    model = Music  # обьединяем модел с таблицой Музик из базы данных
    template_name = 'music_detail.html'  # обьединяем html code
    context_object_name = 'musics'  # даем имя что бы обращатся к базе
    queryset = Music.objects.all()  # вытаскием все модели не все группы а именно модели
