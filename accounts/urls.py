
from django.urls import path
from .views import userRegisterView,log_in_view,UserLogoutView,userBank_accountUpdate,pass_change


urlpatterns = [
  path('register/',userRegisterView.as_view(),name='register'),
  path('login/',log_in_view.as_view(),name='login'),
  path('logout/',UserLogoutView.as_view(),name='logout'),
  path('updateuser/',userBank_accountUpdate.as_view(),name='profile'),
  path("passwordchange/",pass_change.as_view(),name='password')
]
