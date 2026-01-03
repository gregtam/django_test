from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import UserActivity
from .forms import TestUserCreationForm, TestUserChangeForm, UserActivityForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'add_user_activity' in request.POST:
            form = UserActivityForm(request.POST)

            if form.is_valid():
                # User isn't in the form, so we need to save it a different way
                row = form.save(commit=False)
                row.user = request.user
                row.save()

                return redirect('user_test_app:home')
            else:
                print(form.errors)
    else:
        form = UserActivityForm()

    if request.user.is_authenticated:
        user_activity = UserActivity.objects.filter(user=request.user)
    else:
        user_activity = []

    context = {
        'page_name': 'User Test',
        'user_activity': user_activity,
        'form': form
    }

    return render(request, 'user_test_app/home.html', context)


class RegisterView(CreateView):
    form_class = TestUserCreationForm
    template_name = 'user_test_app/register.html'

    success_url = reverse_lazy('login')