import environ
from cryptography.fernet import Fernet
import re

# Initialize environ
env = environ.Env()
environ.Env.read_env()

# Load the Fernet key from environment variable
key = env("FERNET_KEY").encode()  # Ensure it is in bytes
cipher_suite = Fernet(key)

def encrypt_data(data):
    """Encrypt data."""
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    """Decrypt data."""
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

def validate_url(url):
    """Validate the given URL."""
    regex = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None