# create_permissions.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from employees.models import Employee

class Command(BaseCommand):
    help = 'Create permissions for viewing employees'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Employee)
        permission = Permission.objects.create(
            codename='can_view_employees',
            name='Can view employees',
            content_type=content_type,
        )
        self.stdout.write(self.style.SUCCESS('Permission created successfully.'))
