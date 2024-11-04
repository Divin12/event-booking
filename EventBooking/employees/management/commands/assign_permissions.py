from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from employees.models import Employee  # Update with your appropriate model
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'Assign permissions to a group and user'

    def add_arguments(self, parser):
        parser.add_argument('employee_id', type=int, help='Employee ID to assign permission')

    def handle(self, *args, **options):
        permission = Permission.objects.get(codename='can_view_employees')
        
        group = Group.objects.get(name='Managers')  # Replace with the desired group name
        group.permissions.add(permission)
        
        employee_id = options['employee_id']
        employee = Employee.objects.get(pk=employee_id)
        employee.user_permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Permissions assigned successfully.'))
