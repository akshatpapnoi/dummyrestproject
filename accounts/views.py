from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError
from .forms import ProfileForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        profileform = ProfileForm(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('main:dashboard'))

    else:
        userform = UserCreationForm
        profileform = ProfileForm
    return render(request, 'register.html', {'user_form': userform, 'profile_form': profileform})

def user_login(request):
    if request.method == 'POST':
        if Profile.objects.filter(user__username = request.POST['username']).exists():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
            	login(request, user)
            	return HttpResponseRedirect(reverse('main:dashboard'))
            else:
                messages.error(request, 'Invalid credentials. Please try again!')
                return HttpResponseRedirect(reverse('accounts:login'))
    		 
        else:
        	messages.error(request, 'Username does not exists.')
        	return HttpResponseRedirect(reverse('accounts:login'))
    else:
    	if request.user.is_authenticated:
    		return HttpResponseRedirect(reverse('main:dashboard'))
    	else:
    		return render(request, 'login.html', {})



@login_required(login_url=reverse_lazy('accounts:login'))
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))