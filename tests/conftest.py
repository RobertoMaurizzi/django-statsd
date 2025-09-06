import os
import django
from django.conf import settings


# Make sure Django is configured before any tests run
def pytest_configure():
    # Settings are already configured via DJANGO_SETTINGS_MODULE
    # But we can do additional configuration here if needed
    pass