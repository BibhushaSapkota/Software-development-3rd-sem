from pyexpat import model
from django import forms 
from customer.models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("username","customer_address","customer_email","customer_phone","password")
 
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ("__all__")
 
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=("__all__")
