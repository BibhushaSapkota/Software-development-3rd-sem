from django import forms 
from customer.models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("username","customer_address","customer_email","customer_phone","password")
 