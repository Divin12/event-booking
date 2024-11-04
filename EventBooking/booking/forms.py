from datetime import date
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']

        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date:
            if check_in_date <= date.today():
                self.add_error('check_in_date', 'Please select a future date for check-in.')
            if check_out_date <= check_in_date:
                self.add_error('check_out_date', 'Check-out date must be after check-in date.')

        return cleaned_data
