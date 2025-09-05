from django.urls import path

from . import views
from .views import HomePageListView, CreatePost, ShowPost, ReplyView, ShowCats, ProfileView

urlpatterns = [
    path("", HomePageListView.as_view(), name="main"),
    path('create/',CreatePost.as_view(),name='create_post'),
    path('posts/<slug:slug>/', ShowPost.as_view(), name='posts'),
    path('reply/<int:com_id>/', ReplyView.as_view(), name='reply'),
    path('category/<slug:slug>/', ShowCats, name='categories'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]