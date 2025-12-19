from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import DataTable
from .forms import DataForm

# Create your views here.
def home(request):
    return render(request, 'crud_test_app/home.html', {'page_name': 'CRUD'})


def crud(request):
    # objs = DataTable.objects.all()

    form = DataForm()

    if request.method == 'POST':
        # Matches html button name
        if 'add_data' in request.POST:
            form = DataForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('crud_test_app:crud_fbv')

        elif 'update_data' in request.POST:
            item_id = request.POST.get('update_data')
            instance = get_object_or_404(DataTable, id=item_id)
            instance.update()

            form = DataForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('crud_test_app:crud_fbv')

        elif 'delete_data' in request.POST:
            item_id = request.POST.get('delete_data')
            instance = get_object_or_404(DataTable, id=item_id)
            instance.delete()
            return redirect('crud_test_app:crud_fbv')

    return render(request, 'crud_test_app/crud.html')


class CrudView(View):
    # objs = DataTable.objects.all()

    def get(self, request):
        return render(request, 'crud_test_app/crud.html')

    def post(self, request):
        form = DataForm()

        if 'add_data' in request.POST:
            form = DataForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'update_data' in request.POST:
            item_id = request.POST.get('update_data')
            instance = get_object_or_404(DataTable, id=item_id)
            instance.update()

            form = DataForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()

        elif 'delete_data' in request.POST:
            item_id = request.POST.get('delete_data')
            instance = get_object_or_404(DataTable, id=item_id)
            instance.delete()

        return redirect('crud_test_app:crud_cbv')


class ShowDataView(ListView):
    model = DataTable
    template_name = 'crud_test_app/show_data.html'


class AddDataView(CreateView):
    model = DataTable
    template_name = 'crud_test_app/add_data.html'
    fields = ['text']
    success_url = reverse_lazy('crud_test_app:add_data')


class DeleteDataView(DeleteView):
    model = DataTable
    template_name = 'crud_test_app/delete_data.html'
    success_url = reverse_lazy('crud_test_app:show_data')


class UpdateDataView(UpdateView):
    model = DataTable
    fields = ['text']
    template_name = 'crud_test_app/update_data.html'
    success_url = reverse_lazy('crud_test_app:show_data')
