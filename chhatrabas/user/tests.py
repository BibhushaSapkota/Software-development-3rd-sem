from django.test import SimpleTestCase,Client
from django.urls import reverse,resolve
from user.views import *

class TestUrls(SimpleTestCase):
    def test_admindash_url_is_resolved(self):
        url=reverse('admindash')
        self.assertEquals(resolve(url).func, admindash)

    def test_edit_url_is_resolved(self):
        url=reverse('edit',args=[1])
        self.assertEquals(resolve(url).func, edit)

    def test_update_url_is_resolved(self):
        url=reverse('update',args=[1])
        self.assertEquals(resolve(url).func, update)

    def test_delete_url_is_resolved(self):
        url=reverse('delete',args=[1])
        self.assertEquals(resolve(url).func, delete)

class TestViews(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_admindash_views(self):
        response=self.client.get(reverse('admindash'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admin/admindash.html')

    def test_adduser_views(self):
        response=self.client.get(reverse('adduser'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admin/adduser.html')  

    def test_review_views(self):
        response=self.client.get(reverse('review'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hostel/review.html')
