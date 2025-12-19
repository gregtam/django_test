from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import TestUserCreationForm, TestUserChangeForm

# Create your views here.
def home(request):
    return render(request,  'user_test_app/home.html', {'page_name': 'User Test'})


class RegisterView(CreateView):
    form_class = TestUserCreationForm
    template_name = 'user_test_app/register.html'

    success_url = reverse_lazy('login')
