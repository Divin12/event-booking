from django.contrib.auth.models import User
from django.db import models
from apartment.models import Apartment  # Import the Apartment model

class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Field to store the calculated price

    def save(self, *args, **kwargs):
        # Calculate the number of months between check-in and check-out dates
        num_of_months = (self.check_out_date.year - self.check_in_date.year) * 12
        num_of_months += self.check_out_date.month - self.check_in_date.month

        # Assuming price_per_night is a field in the Apartment model
        price_per_night = self.apartment.price_per_night  # Adjust with the correct field name
        total_price = num_of_months * price_per_night

        self.price = total_price  # Assign the calculated total price to the price field
        super(Booking, self).save(*args, **kwargs)