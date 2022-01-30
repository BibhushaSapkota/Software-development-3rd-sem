from django.db import models

# Create your models here.
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