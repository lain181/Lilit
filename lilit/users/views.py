from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Authorisation"}
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('main')
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registrate.html'
    extra_context = {'title':'Registration'}
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('main')

    def form_valid(self, form):
        #сохранение формы и создание объекта пользователя ( self.object).
        response = super().form_valid(form)
        #Функция login()принимает текущий запрос и недавно созданный объект пользователя ( self.object)
        login(self.request, self.object)
        # Перенаправление на et_success_url
        return response

def logout_user(request):
    logout(request)
    return(redirect('main'))

# Create your views here.
