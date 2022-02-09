from django.db import models

# Create your models here.
class Hostel(models.Model):
    hostel_id=models.AutoField(auto_created=True,primary_key=True)
    customer_id=models.CharField(max_length=100)
    customername=models.CharField(max_length=100)
    price=models.CharField(max_length=200)
    date=models.DateField(max_length=20)
    hostel_name=models.CharField(max_length=100)
    class Meta:
            db_table="hostel"
            
class Reviews(models.Model):
    username=models.CharField(max_length=200)
    hostelname=models.CharField(max_length=200)
    review=models.CharField(max_length=5000)
    class Meta:
        db_table="reviews"