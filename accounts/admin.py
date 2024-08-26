from django.contrib import admin
from accounts.models import user_Address,UserBankAccount
# Register your models here.
admin.site.register(user_Address)
admin.site.register(UserBankAccount)
