from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, DateTimeField, IntegerField
from .user     import User


class account(models.Model):
    id  = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CharField)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive    = models.BooleanField(default=True)
