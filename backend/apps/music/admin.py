from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'public_date',
        'text_song',
        'music',
        'group'
    ]
    filter_horizontal = [
        'singer',
        'genre',
    ]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
    ]
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'photo',
        'biography',
        'created_date'
    ]
    filter_horizontal = [
        'singer',
    ]

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'nickname',
        'photo',
        'biography'
    ]


