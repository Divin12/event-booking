from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from apartment.models import Apartment



@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


from django.shortcuts import render
from .models import Employee

def employee_detail_view(request, employee_name):
    employee = Employee.objects.get(name=employee_name)  # Assuming 'name' is the primary key
    return render(request, 'employee_detail.html', {'employee': employee})


from .forms import EmployeeForm

def add_employee_with_apartments(request):
    apartments = Apartment.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the list of employees
    else:
        form = EmployeeForm()
    return render(request, 'add_employee_with_apartments.html', {'apartments': apartments, 'form': form})



