from django.db import models
from authentication.models import User
from home.models import Home
# Create your models here.
class Transaction(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, default=1)
    tenant_user = models.ForeignKey(User,on_delete=models.CASCADE, default=1, related_name='tenant_user_transaction')
    landlord_user = models.ForeignKey(User,on_delete=models.CASCADE, default=1, related_name='landlord_user_transation')
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=50, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transactions"
