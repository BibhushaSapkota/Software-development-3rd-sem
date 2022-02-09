from django.db import models

# Create your models here.
<<<<<<< HEAD

=======
class User(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100,default="admin")
    email = models.CharField(max_length=100,unique=True,default="admin@gmail.com")
    password=models.CharField(max_length=8,default="admin")

    class Meta:
        db_table="users"
>>>>>>> 3a36dd477292d440b7c32cda54324876d84465ff
