from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from .forms import AddCommentForm
from .models import (Post, Comment, Category)


class HomePageListView(ListView):
     model=Post
     template_name = 'main/home_page.html'
     context_object_name = 'posts'
     extra_context = {
          'title': 'Main Page',
     }

def ShowCats(request, slug):
     a=get_object_or_404(Category, slug=slug)
     b=Post.objects.filter(category=a)
     data={'title':a,
           'cat': b
           }
     return render(request,'main/category.html', data)

class CreatePost(CreateView):
     model = Post
     template_name = 'main/create_post.html'
     fields = ['name','content','category']


     extra_context = {'title':'Create post'}

     def form_valid(self, form):
          form.instance.author=self.request.user
          return super().form_valid(form)


class ProfileView(DetailView):
     model = User
     template_name = 'main/profile.html'
class ShowPost(View):
     def get(self, request, slug):
          post = get_object_or_404(Post, slug=slug)
          form = AddCommentForm()
          comms = post.com_of_post.all()

          return render(request, 'main/post.html', {'post': post, 'form': form, 'com':comms})

     def post(self, request, slug):
          post = get_object_or_404(Post, slug=slug)
          form = AddCommentForm(request.POST)

          if form.is_valid():
               comment = form.save(commit=False)
               form.instance.comment_author = self.request.user
               comment.comment_post = post
               comment.save()
               return redirect('posts',slug)  # Перенаправление на детальную страницу поста
          return render(request, 'main/post.html', {'post': post, 'form': form})

class ReplyView(CreateView):
     model = Comment
     template_name = "main/reply.html"

     def get_success_url(self):
          next_url = self.request.GET.get('next')
          if next_url:
               return next_url
          return reverse_lazy('main')
     fields = ['comment_content']

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['com_id']=self.kwargs['com_id']
          context['com_name']=get_object_or_404(Comment, pk=self.kwargs['com_id'])
          return context

     def form_valid(self, form):
          reply_com = get_object_or_404(Comment, pk=self.kwargs['com_id'])
          form.instance.comment_author=self.request.user
          form.instance.reply=reply_com
          return super().form_valid(form)

