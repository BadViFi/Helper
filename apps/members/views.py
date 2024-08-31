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
from django.contrib.auth.models import User
from .forms import UserCreateForm
from django.contrib import messages
from apps.additions.models import Favorite
from apps.additions.forms import PostForm
from django.contrib.auth import login



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'members/login.html'

class LogoutUser(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Ви вийшли з системи')
        return redirect('members:login')


class SignUpView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'members/signup.html'
    success_url = reverse_lazy('members:profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Ви успішно зареєструвалися як {user.username}')
        
        return redirect(self.success_url)

class ProfileView(View):
    template_name = 'members/profile.html'

    def get(self, request, username=None):
        
        if not request.user.is_authenticated:
            return redirect('members:login')

        
        if username is None:
            username = request.user
        
        
        if request.user == username:
            another_user = False
        else:
            another_user = True
        
 
        fav = Favorite.objects.filter(user=request.user)
        favorite_additions = Favorite.objects.filter(user=request.user).values_list('addition_id', flat=True)
        
  
        context = {
            'favorites': fav,
            'another_user': another_user,
            'form': PostForm(),
            'favorite_additions': favorite_additions,
        }
        
        return render(request, self.template_name, context)
