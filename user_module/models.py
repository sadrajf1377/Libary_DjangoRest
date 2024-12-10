from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    number=models.CharField(max_length=10,verbose_name='users phone number')
    balance = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='users balance', default=00.00)




