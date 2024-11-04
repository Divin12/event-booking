from django.db import models
from employees.models import Employee



class Apartment(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=100, null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='apartment_images/', null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    