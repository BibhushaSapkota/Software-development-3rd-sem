from django.db import models

# Create your models here.
class Hostel(models.Model):
    
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    customer_username=models.CharField(max_length=100)
    customer_address=models.CharField(max_length=100)
    customer_email=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=10)
    customer_password=models.CharField(max_length=100)
    class Meta:
        db_table="customer"
