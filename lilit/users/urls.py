from django.urls import path

from . import views
from .views import LoginUser, RegisterUser

app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registrate/', RegisterUser.as_view(), name='registrate'),
]