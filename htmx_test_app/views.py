from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Counter
from .forms import CountForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'increase_count' in request.POST:
                existing_row, created = Counter.objects.get_or_create(user=request.user)
                existing_row.count += 1
                existing_row.save()

        # Filters the data on the logged in user
        counter_model = Counter.objects.filter(user=request.user)

        return render(request, 'htmx_test_app/home.html', {'button_status': 'OFF', 'counter': counter_model})

    else:
        return render(request, 'htmx_test_app/home.html', {})

def increase_count(request):
    row = Counter.objects.get(user=request.user)
    row.count += 1
    row.save()

    return HttpResponse(row.count)


def htmx_button_view_url(request, button_text):
    return render(request, 'htmx_test_app/partials/button_result.html', {'button_text': button_text})


def htmx_button_view_htmx(request):
    button_text = request.GET.get('button_text')
    return render(request, 'htmx_test_app/partials/button_result.html', {'button_text': button_text})


def htmx_button_toggle(request, button_status):
    return render(request, 'htmx_test_app/partials/simple_button_result.html', {'button_status': button_status})