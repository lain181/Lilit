from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import (Post)


class HomePageListView(ListView):
     model=Post
     template_name = 'main/home_page.html'
     context_object_name = 'posts'
     extra_context = {
          'title': 'Main Page',
     }

class CreatePost(CreateView):
     model = Post
     template_name = 'main/create_post.html'
     fields = ['name','content','category']
     success_url = reverse_lazy('main')
     extra_context = {'title':'Create post'}

     def form_valid(self, form):
          form.instance.author=self.request.user
          return super().form_valid(form)

class ShowPost(DetailView):
     model = Post
     template_name = 'main/post.html'
     context_object_name = 'post'
