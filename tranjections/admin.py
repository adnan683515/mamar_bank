from django.contrib import admin
from . models import Transaction
from tranjections.views import send_email_msg
# Register your models here.


@admin.register(Transaction)


class TranjectionModelAdmin(admin.ModelAdmin):
    list_display = ['account','amount','balance_after_transaction','transaction_type','loan_approve']
    
    def save_model(self,request,obj,form,change):
        if obj.loan_approve:
            obj.account.balance += obj.amount
            obj.balance_after_transection = obj.account.balance
            
            obj.account.save()
            send_email_msg('Loan Reqeust Successfully',obj.account.user,obj.amount,request.user.email,'tranjections/loan_approvemsg.html')
        super().save_model(request,obj,form,change)