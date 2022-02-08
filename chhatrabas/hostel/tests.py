from django.test import SimpleTestCase
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from hostel.views import *

class TestUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url=reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_redirect)

    def test_dashboard_url_is_resolved(self):
        url=reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)