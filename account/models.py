from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, related_name='user_account', on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone = models.IntegerField(max_length=11)
    billing_address = models.CharField(max_length=250)
    is_closed = models.BooleanField(default=False)
    open = models.DateField(auto_now_add=True)
    closed = models.DateField(auto_now=True)
    new = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)    
    def __str__(self):
        return str(self.user.username)
    