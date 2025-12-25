from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'htmx_test_app/home.html', {'button_status': 'OFF'})


def htmx_button_view_url(request, button_text):
    return render(request, 'htmx_test_app/partials/button_result.html', {'button_text': button_text})


def htmx_button_view_htmx(request):
    button_text = request.GET.get('button_text')
    return render(request, 'htmx_test_app/partials/button_result.html', {'button_text': button_text})


def htmx_button_toggle(request, button_status):
    return render(request, 'htmx_test_app/partials/simple_button_result.html', {'button_status': button_status})