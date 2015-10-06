from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length = 10)
    email = models.CharField(max_length = 40)
    password = models.CharField(max_length = 150)
    salt = models.CharField(max_length = 150)
    state = models.IntegerField()
    rol = models.CharField(max_length = 40)
    register_date = models.DateTimeField(auto_now_add=True)
    last_conected = models.DateTimeField(auto_now=True)
    
    
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    points = models.IntegerField()