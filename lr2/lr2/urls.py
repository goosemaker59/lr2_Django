from django.urls import path
from playlists import views

urlpatterns = [
    path('', views.index),
]