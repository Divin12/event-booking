# scripts/setup_roles.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apartment.models import Apartment  # Adjust 'myapp' to your app name

def setup_roles():
    manager_group, created = Group.objects.get_or_create(name='Manager')
    renter_group, created = Group.objects.get_or_create(name='Renter')

    # Example permission setup
    view_perm = Permission.objects.get(codename='view_apartment', content_type=ContentType.objects.get_for_model(Apartment))
    manage_perm = Permission.objects.get(codename='change_apartment', content_type=ContentType.objects.get_for_model(Apartment))

    manager_group.permissions.add(view_perm, manage_perm)
    renter_group.permissions.add(view_perm)
