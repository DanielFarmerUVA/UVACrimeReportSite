import os
from django.test import SimpleTestCase
from buildexample import settings

class TestSettings(SimpleTestCase):
    # testing some of the settings
    def test_debug_mode(self):
        """
        test that DEBUG mode is enabled in development.
        """
        self.assertTrue(settings.DEBUG, "DEBUG mode is not enabled.")

    def test_static_files_configuration(self):
        """
        test that STATIC_ROOT and STATIC_URL are properly configured.
        """
        self.assertTrue(settings.STATIC_ROOT, "STATIC_ROOT is not defined in settings.")
        self.assertTrue(settings.STATIC_URL, "STATIC_URL is not defined in settings.")