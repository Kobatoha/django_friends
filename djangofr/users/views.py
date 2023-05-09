from django.views import View
from users.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from .models import *


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileDetail(DetailView):
    '''Профиль пользователя'''
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return self.request.user.profile
        else:
            return None


def profile_error(request):
    return render(request, 'users/profile-error.html')
