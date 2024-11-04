# employees/urls.py

from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.add_employee_with_apartments, name='add_employee'),
    path('<str:employee_name>/', views.employee_detail_view, name='employee_detail'),
    path('', views.employee_list, name='employee_list'),
]
