from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse(views.home)
        self.assertEquals(resolve(url).func, views.home)

    def test_logout_url_resolves(self):
        url = reverse(views.logout_view)
        self.assertEquals(resolve(url).func, views.logout_view)

    def test_report_url_resolves(self):
        url = reverse(views.report)
        self.assertEquals(resolve(url).func, views.report)

    def test_success_url_resolves(self):
        url = reverse(views.report_upload)
        self.assertEquals(resolve(url).func, views.report_upload)

    def test_anon_home_url_resolves(self):
        url = reverse(views.anon_home)
        self.assertEquals(resolve(url).func, views.anon_home)

    def test_admin_home_url_resolves(self):
        url = reverse(views.admin_home)
        self.assertEquals(resolve(url).func, views.admin_home)
