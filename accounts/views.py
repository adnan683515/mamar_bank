from django.shortcuts import render,redirect
from accounts.forms import userRegisterForm, UserUpdateForm
from django.views.generic import FormView
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

class userRegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = userRegisterForm
    success_url = reverse_lazy('register')
    
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) #form valid function call hobe jkhn sob data valid hobe
    
 
    
class log_in_view(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class userBank_accountUpdate(View):
    template_name = 'accounts/profile.html'
    
    def get(self,request):
        form = UserUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = UserUpdateForm(request.POST,request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name,{'form':form})
    
    
class pass_change(PasswordChangeView):
    form_class= PasswordChangeForm
    template_name = 'accounts/password.html'
    success_url = reverse_lazy('login')
    title = "Password Change"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_data"] = self.title
        return context
    
    def form_valid(self, form):
            mail_subjects = "Password Change"
            messagee = render_to_string('accounts/password_mgs.html',{
                'user':self.request.user,
                

            })
        
            too_email = self.request.user.email
                        
            sends_email = EmailMultiAlternatives(mail_subjects," ",to=[too_email])
            sends_email.attach_alternative(messagee,'text/html')
            sends_email.send()
            

            messages.success(self.request,"Your password Change successfull.")
            return super().form_valid(form)
    
   