from django.urls import path
from .views import *

urlpatterns = [
    path('singer/list/', SingersView.as_view(), name='singers'),
    path('group/list/', GroupsView.as_view(), name='groups'),
    path('group/detail/<int:pk>/', GroupsDetailView.as_view(), name='group_detail'),
    path('singer/detail/<int:pk>/', SingerDetailView.as_view(), name='singer_detail'),
    path('music/list/', MusicListView.as_view(), name='music_list'),
    path('music/detail/<int:pk>/', MusicDetailView.as_view(), name='music_detail'),
]
