from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

# With function based views, variables are easy to fill in.
def home(request):
    return render(request, 'test_app/home.html', {'page_name': 'home'})


def test(request):
    return render(request, 'test_app/home.html', {'page_name': 'test'})


def about(request):
    return render(request, 'test_app/about.html', {'page_name': 'about'})


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test_app/home.html', {'page_name': 'test class'})


class TestTemplateView(TemplateView):
    template_name = 'test_app/home.html'
    page_name = 'Test Template'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_name'] = 'test template view'

        return context
