from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import UserCreateForm
from django.contrib import messages
# Create your views here.

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'members/login.html'

    

class LogoutUser(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Ви вийшли з системи')
        return redirect('members:login')
    
    
class SignUpView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'members/signup.html'
    success_url = reverse_lazy('main:index')
    
    
    
    
class ProfileView(TemplateView):
    template_name = 'members/profile.html'
    
# def profile_view(request):
#     return render(request, 'members/profile.html')