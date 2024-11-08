# myapp/tests/test_logging.py
import logging
from django.test import TestCase

class LoggingTest(TestCase):
    def test_warning_logging(self):
        logger = logging.getLogger('django')
        logger.warning('Test Warning')
        # Check your log file manually or set up automated log validation
