from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

