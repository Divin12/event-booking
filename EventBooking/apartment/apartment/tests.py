import re
from django.test import TestCase
from django.contrib.auth.models import User, Group
from apartment.utils.security import encrypt_data, decrypt_data, validate_url
from django.urls import reverse
from django.conf import settings
from .models import Apartment




class AccessControlTest(TestCase):
    def setUp(self):
        # Set up an Apartment instance with necessary fields
        self.apartment = Apartment.objects.create(
            name="TestApartment",
            price_per_month=1000,
            price_per_night=100
        )

        # Set up manager user and group
        self.manager_user = User.objects.create_user(username='manager', password='password')
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        manager_group.user_set.add(self.manager_user)

        # Set up a non-manager user
        self.non_manager_user = User.objects.create_user(username='non_manager_user', password='password')

    def test_manager_access(self):
        # Log in as manager
        self.client.login(username='manager', password='password')
        
        # Attempt to access apartment detail view
        response = self.client.get(reverse('apartment_detail', args=[self.apartment.name]))
        self.assertEqual(response.status_code, 200)  # Expect successful access for manager

    def test_renter_access(self):
        # Log in as a user without Manager access
        self.client.login(username='non_manager_user', password='password')
        
        # Attempt to access the apartment detail view
        response = self.client.get(reverse('apartment_detail', args=[self.apartment.name]))
        self.assertEqual(response.status_code, 403)  # Expect forbidden for non-manager user

class EncryptionTest(TestCase):
    def test_encryption(self):
        data = "Sensitive Information"
        encrypted = encrypt_data(data)
        decrypted = decrypt_data(encrypted)
        self.assertEqual(decrypted, data)

class InjectionProtectionTest(TestCase):
    def setUp(self):
        self.apartment = Apartment.objects.create(
            name="TestApartment",
            price_per_month=1000,
            price_per_night=100
        )

    def test_sql_injection_protection(self):
    # Test with safe parameters
        response = self.client.get(reverse('apartment_detail', args=[self.apartment.name]), {'id': '1 OR 1=1'})
        self.assertNotContains(response, "SQL syntax error") 


class SecurityConfigurationTest(TestCase):
    def test_debug_off_in_production(self):
        self.assertFalse(settings.DEBUG, "DEBUG mode should be off in production.")

class AuthenticationTest(TestCase):
    def test_password_strength(self):
        user = User.objects.create_user(username="testuser", password="simple")
        self.assertTrue(len(user.password) > 8, "Password is too weak")
        # Check if weak passwords are rejected based on your policy

class SSRFProtectionTest(TestCase):
    def test_validate_url(self):
        valid_url = "https://example.com"
        invalid_url = "ftp://malicious.com"
        self.assertTrue(validate_url(valid_url))
        self.assertFalse(validate_url(invalid_url))