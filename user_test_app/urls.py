from django.contrib import admin
from django.urls import path, include
from .views import RegisterView
from . import views

app_name = 'user_test_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', RegisterView.as_view(), name='register')
]
