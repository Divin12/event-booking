# myapp/tests/test_file_uploads.py
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apartment.utils.security import hash_file

class FileHashTest(TestCase):
    def test_hash_file(self):
        file = SimpleUploadedFile("file.txt", b"Hello world")
        file_hash = hash_file(file)
        
