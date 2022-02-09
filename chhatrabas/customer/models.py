from statistics import mode
from django.db import models

# Create your models here.
class Contactus(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=5000)
    class Meta:
        db_table="contact"
        
class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100)
    customer_address=models.CharField(max_length=100)
    customer_email=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    last_login=models.DateTimeField(null=True)
    class Meta:
            db_table="customer"

class Billing(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    customer_name=models.CharField(max_length=100)
    hostel_name=models.CharField(max_length=100)
    start_date=models.DateField(max_length=20)
    end_date=models.DateField(max_length=20)
    total_paid=models.CharField(max_length=10)
    class Meta:
        db_table="bill"