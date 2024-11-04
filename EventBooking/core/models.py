from django.db import models

# class Employe(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.BigIntegerField()
#     number = models.BigIntegerField()
#     address = models.BigIntegerField()
#     email = models.BigIntegerField()
#     function = models.BigIntegerField()

# class CreateEvent(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     apart_name = models.CharField(max_length=255)
#     apart_address = models.CharField(max_length=255)
#     image = models.CharField(max_length=255)
#     adate = models.DateField()
#     avenue = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     approve = models.CharField(max_length=255)

# class RegisterUser(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     number = models.IntegerField()
#     password = models.CharField(max_length=255)

# class BookApartment(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     user_name = models.CharField(max_length=255)
#     user_number = models.CharField(max_length=255)
#     user_email = models.CharField(max_length=255)
#     total_member = models.CharField(max_length=255)
#     location_name = models.CharField(max_length=255)
#     event_date = models.DateField()

# class ImageAdd(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     img_title = models.CharField(max_length=255)
#     img_location = models.CharField(max_length=255)
#     img_desc = models.CharField(max_length=255)

# class User(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     date_birth = models.DateField()
#     regist_date = models.BigIntegerField()

# class PasswordReset(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     email = models.CharField(max_length=255)
#     new_pass = models.CharField(max_length=255)

class Admin(models.Model):
    admin_name = models.CharField(max_length=255)
    admin_email = models.CharField(max_length=255)

# class ApartLocation(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     a_name = models.BigIntegerField()
#     apart_addres = models.BigIntegerField()
#     manager_name = models.BigIntegerField()
#     manager_num = models.BigIntegerField()

    # employe = models.ForeignKey(Employe, on_delete=models.CASCADE)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['id'], name='unique_id')
    #     ]
        
        

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # Add other fields as needed
