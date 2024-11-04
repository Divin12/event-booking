from django.shortcuts import render

# admin_dashboard/views.py
from django.shortcuts import render
from .models import Apartment, Message

def admin_dashboard(request):
    available_apartments = Apartment.objects.filter(availability=True).count()
    booked_apartments = Apartment.objects.filter(booked=True).count()
    apartment_list = Apartment.objects.all()
    message_list = Message.objects.all()

    context = {
        'available_apartments': available_apartments,
        'booked_apartments': booked_apartments,
        'apartment_list': apartment_list,
        'message_list': message_list,
    }
    return render(request, 'admin_dashboard/dashboard.html', context)
