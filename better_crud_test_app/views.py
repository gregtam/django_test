from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import DataTable
from .forms import DataForm

def home_view(request):
    # 1. Logic for the "Add" button (POST)
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecting back to 'home' clears the form and prevents 
            # duplicate submissions if the user refreshes the page.
            return redirect('better_crud_test_app:home') 
    else:
        # 2. Logic for the initial page load (GET)
        form = DataForm()

    # 3. Always fetch the items for the table
    # We put newest items at the top so the user sees their "Add" immediately
    items = DataTable.objects.all().order_by('-id')
    
    context = {
        'items': items,
        'add_form': form,
        'page_name': 'Better CRUD'
    }
    return render(request, "better_crud_test_app/home.html", context)


class ItemUpdateView(UpdateView):
    model = DataTable
    fields = ['text']
    template_name = "better_crud_test_app/item_update.html"
    success_url = reverse_lazy('better_crud_test_app:home')  # Returns to your dashboard after saving


class ItemDeleteView(DeleteView):
    model = DataTable
    template_name = "better_crud_test_app/item_confirm_delete.html"
    success_url = reverse_lazy('better_crud_test_app:home')  # Returns to your dashboard after deleting