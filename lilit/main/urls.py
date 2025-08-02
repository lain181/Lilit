from django.urls import path

from . import views
from .views import HomePageListView, CreatePost, ShowPost

urlpatterns = [
    path("", HomePageListView.as_view(), name="main"),
    path('create/',CreatePost.as_view(),name='create_post'),
    path('posts/<slug:slug>/', ShowPost.as_view(), name='posts')
]