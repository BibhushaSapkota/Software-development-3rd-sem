
from django.test import SimpleTestCase
from django.urls import reverse,resolve

from customer.views import *

class TestUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url=reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_redirect)

    def test_home_url_is_resolved(self):
        url=reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
    
    def test_blog_url_is_resolved(self):
        url=reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog)

    def test_contact_url_is_resolved(self):
        url=reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact )

    def test_hostel_url_is_resolved(self):
        url=reverse('hostel')
        print(resolve(url))
        self.assertEquals(resolve(url).func, hostel)

    def test_hostelprofile_url_is_resolved(self):
        url=reverse('hostelprofile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, hostelprofile)

    def test_userprofile_url_is_resolved(self):
        url=reverse('userprofile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userprofile)

    def test_signout_url_is_resolved(self):
        url=reverse('signout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signout)

    def test_billing_url_is_resolved(self):
        url=reverse('billing')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bill)