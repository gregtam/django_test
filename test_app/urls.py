from django.urls import path, include
from . import views
from .views import TestView, TestTemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('test_class/', TestView.as_view(), name='test_class'),
    path('test_template_class/', TestTemplateView.as_view(), name='test_template_class')
]
