import imp
from django.http import response
from django.test import TestCase,Client
from django.urls import reverse
from customer.models import Customer
import json

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()

    def test_register_GET(self):
        response=self.client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'customer/registration.html')

    def test_login_GET(self):
        response=self.client.get(reverse('login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'customer/signin.html')

    

