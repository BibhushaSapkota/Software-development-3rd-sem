from django.db import models
from customer.models import Customer
# Create your models here.
class Hostel(models.Model):
    hostel_id=models.AutoField(auto_created=True,primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    hostel_name=models.CharField(max_length=100)
    booking_date=models.DateField(max_length=200)
    price=models.CharField(max_length=10)
    class Meta:
        db_table="hostel"
