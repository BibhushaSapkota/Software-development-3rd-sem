

import imp
from django.test import TestCase

from chhatrabas.customer.models import Customer
from django.test import TestCase
from customer.models import Customer

class TestModels(TestCase):
    def setUp(self): 
        self.customer1=Customer.objects.create(
            username='optimus',
            customer_address='chabahil',
            customer_email='sahg@aks.com',
            customer_phone='1234567890',
            password='helicopter'
        )

