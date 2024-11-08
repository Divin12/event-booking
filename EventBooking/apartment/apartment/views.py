from django.shortcuts import render, get_object_or_404
from .models import Apartment
from django.shortcuts import render
from django.http import HttpResponse


def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment/apartment_list.html', {'apartments': apartments})

def apartment_detail(request, apartment_name):
    apartment = get_object_or_404(Apartment, pk=apartment_name)
    return render(request, 'apartment/apartment_list.html', {'apartments': apartment})

# def apartment_detail_view(request, apartment_name):
#     apartment = Apartment.objects.get(pk=apartment_name)
#     # Assuming you're getting the associated employee for this apartment
#     employee = apartment.employee  # Accessing the associated employee
#     return render(request, 'apartment_detail.html', {'apartment': apartment, 'employee': employee})

from .models import Apartment

def apartment_detail_view(request, apartment_name):
    try:
        # Fetch the apartment using its name
        apartment = Apartment.objects.get(name=apartment_name)
        # Get associated employee or related data as needed

        return render(request, 'apartment/apartment_detail.html', {'apartment': apartment})
    except Apartment.DoesNotExist:
        # Handle case where the apartment with the given name does not exist
        return HttpResponse("Apartment not found", status=404)
    
    
from django.shortcuts import render
from .models import Apartment

def apartment_name_list_view(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment/apartment_name.html', {'apartments': apartments})


def view_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    return apartment