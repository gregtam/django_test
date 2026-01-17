from django.urls import path, include
from . import views

app_name = 'htmx_test_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('increase_count', views.increase_count, name='increase_count'),
    path('htmx_button_url/<str:button_text>', views.htmx_button_view_url, name='htmx_button_url'),
    path('htmx_button_htmx', views.htmx_button_view_htmx, name='htmx_button_htmx'),
    path('htmx_button_toggle/<str:button_status>', views.htmx_button_toggle, name='htmx_button_toggle'),
]