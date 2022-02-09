from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100,default="admin")
    email = models.CharField(max_length=100,unique=True,default="admin@gmail.com")
    password=models.CharField(max_length=8,default="admin")

    class Meta:
        db_table="users"
