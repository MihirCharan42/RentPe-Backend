from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "user" 