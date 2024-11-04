from django.db import models

# Create your models here.

# admin_dashboard/models.py

class Apartment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    booked = models.BooleanField(default=False)
    # Add more fields as needed

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"

