from django.test import SimpleTestCase,Client
from django.urls import reverse,resolve
from hostel.views import *

class TestUrls(SimpleTestCase):
    def test_book_url_is_resolved(self):
        url=reverse('hostelbook')
        self.assertEquals(resolve(url).func, hostelbook)

    def test_review_url_is_resolved(self):
        url=reverse('review')
        self.assertEquals(resolve(url).func, hostelreview)

class TestViews(SimpleTestCase):
    def setUp(self):
        self.client=Client()
    def test_review_GET(self):
        response=self.client.get(reverse('review'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"hostel/review.html")
