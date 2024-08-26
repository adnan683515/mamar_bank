
from django.urls import path
from tranjections.views import LoanListView, WithdrawMoneyView,DepositMoneyView,LoanRequestView,TransactionReportView,PayLoanView,TransferView




urlpatterns = [
    path("DepositeMoney/",DepositMoneyView.as_view(),name="deposit_money"),
    path("report/",TransactionReportView.as_view(),name="tranjection_report"),
    path('withdraw/',WithdrawMoneyView.as_view(),name='withdraw_money'),
    path("loan_request/",LoanRequestView.as_view(),name="loan_reqeust"),
    path("loans/",LoanListView.as_view(),name="loan_list"),
    path("loan/<int:loan_id>/",PayLoanView.as_view(),name="payloan"),
    path("transfer/",TransferView.as_view(),name="transfer_form")
    
]
