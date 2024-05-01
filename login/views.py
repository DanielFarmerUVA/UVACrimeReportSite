from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'login/login.html')
# Create your views here.
