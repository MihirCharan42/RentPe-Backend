from django.db import models
from authentication.models import User
# Create your models here.
class Home(models.Model):
    description = models.CharField(max_length=2500)
    address = models.CharField(max_length=250)

    tenant_user = models.ForeignKey(User,on_delete=models.CASCADE, default=1, related_name='tenant_user')
    tenant_name = models.CharField(max_length=50)
    tenant_phone = models.CharField(max_length=15)

    landlord_user = models.ForeignKey(User,on_delete=models.CASCADE, default=1, related_name='landlord_user')
    landlord_name = models.CharField(max_length=50)
    landlord_phone = models.CharField(max_length=15)

    rent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    images = models.JSONField(default=dict)
    
    class Meta:
        db_table = "home"