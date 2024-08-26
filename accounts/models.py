from django.db import models
from django.contrib.auth.models import User
from accounts.constance import ACCOUNT_TYPE,GENDER_TYPE
# Create your models here.




#django  amader  built in user make korar facility dey
class UserBankAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='account') 
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True) 
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2) # akjon user 12 digit opdi tk rakte parbe decimal place hocce 2 dosomik opdi rakte parbe 1000.50
    bankdurft = models.BooleanField(default=True,null=True,blank=True)
    
    def __str__(self):
        return str(self.account_no)
    
    
class user_Address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='address')
    street_address =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.email
    