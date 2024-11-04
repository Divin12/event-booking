from django.contrib import admin

from .models import Employee
from apartment.models import Apartment  # Import the Apartment model

class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ApartmentInline]