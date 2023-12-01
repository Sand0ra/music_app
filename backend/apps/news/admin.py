
from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'public_date', 'description',]
    filter_horizontal = ['photos']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image',]
