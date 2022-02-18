
from django.test import SimpleTestCase
from django.urls import reverse,resolve

from customer.views import *

class TestUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func, login_redirect)

    def test_home_url_is_resolved(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_blog_url_is_resolved(self):
        url=reverse('blog')
        self.assertEquals(resolve(url).func, blog)

    def test_contact_url_is_resolved(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func, contact )

    def test_hostel_url_is_resolved(self):
        url=reverse('hostel')
        self.assertEquals(resolve(url).func, hostel)

    def test_hostelprofile_url_is_resolved(self):
        url=reverse('hostelprofile')
        self.assertEquals(resolve(url).func, hostelprofile)

    def test_userprofile_url_is_resolved(self):
        url=reverse('userprofile')
        self.assertEquals(resolve(url).func, userprofile)

    def test_signout_url_is_resolved(self):
        url=reverse('signout')
        self.assertEquals(resolve(url).func, signout)

    def test_billing_url_is_resolved(self):
        url=reverse('billing')
        self.assertEquals(resolve(url).func, bill)