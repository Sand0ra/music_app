
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
