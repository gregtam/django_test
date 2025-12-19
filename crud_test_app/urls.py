from django.urls import path, include
from . import views
from .views import CrudView, ShowDataView, AddDataView, DeleteDataView, UpdateDataView
from . import views

app_name = 'crud_test_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('crud_fbv', views.crud, name='crud_fbv'),
    path('crud_cbv', CrudView.as_view(), name='crud_cbv'),
    path('show_data/', ShowDataView.as_view(), name='show_data'),
    path('add_data/', AddDataView.as_view(), name='add_data'),
    path('delete_data/<int:pk>', DeleteDataView.as_view(), name='delete_data'),
    path('update_data/<int:pk>', UpdateDataView.as_view(), name='update_data')
]
