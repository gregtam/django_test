from django.urls import path
from . import views
from .views import ItemUpdateView, ItemDeleteView

app_name = 'better_crud_test_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('update/<int:pk>', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ItemDeleteView.as_view(), name='delete'),
]