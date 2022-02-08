from django.test import SimpleTestCase
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from user.views import *

class TestUrls(SimpleTestCase):
    def test_admindash_url_is_resolved(self):
        url=reverse('admindash')
        print(resolve(url))
        self.assertEquals(resolve(url).func, admindash)

    def test_edit_url_is_resolved(self):
        url=reverse('edit')
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit)

    def test_update_url_is_resolved(self):
        url=reverse('update/1')
        print(resolve(url))
        self.assertEquals(resolve(url).func, update/1)

    def test_delete_url_is_resolved(self):
        url=reverse('delete')
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete)