from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SiteUserForm
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser
from django.core.exceptions import ValidationError


# Create your views here.
def register(request):
    if request.method == 'POST':
        print('post')
        userform = UserCreationForm(request.POST)
        siteuserform = SiteUserForm(request.POST)

        if userform.is_valid() and siteuserform.is_valid():
            print('valid form')
            user = userform.save()
            siteuser = siteuserform.save(commit=False)
            siteuser.user = user
            siteuser.save()
            return HttpResponseRedirect(reverse('main:dashboard'))

    else:
        userform = UserCreationForm
        siteuserform = SiteUserForm
    return render(request, 'register.html', {'user_form': userform, 'user_profile_form': siteuserform})

def user_login(request):
    if request.method == 'POST':
        if SiteUser.objects.filter(user__username = request.POST['username']).exists():
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