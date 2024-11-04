# urls.py in the booking app
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('list_apartments/', views.list_available_apartments, name='list_apartments'),
    path('book_apartment/<int:apartment_id>/', views.book_apartment, name='book_apartment'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),
    # Other URL patterns
]
