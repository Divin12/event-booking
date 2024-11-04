# views.py in the booking app
from django.shortcuts import render, redirect
from .models import Booking
from apartment.models import Apartment  # Import the Apartment model
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from apartment.models import Apartment  # Import the Apartment model

@login_required
def list_available_apartments(request):
    apartments = Apartment.objects.all()  # Retrieve a list of available apartments
    return render(request, 'list_apartments.html', {'apartments': apartments})

@login_required
def book_apartment(request, apartment_id):
    apartment = Apartment.objects.get(pk=apartment_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.apartment = apartment  # Assign the apartment to the booking
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.save()
            return redirect('booking:user_bookings')  # Redirect to user's bookings after successful booking
    else:
        form = BookingForm()

    return render(request, 'book_apartment.html', {'form': form, 'apartment': apartment})


def user_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user_bookings.html', {'user_bookings': user_bookings})