from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User


# Create your views here.

def index(request):
    return render(request, 'appTwo/index.html')


def users(request):
    # THIS AINT WORKING
    return render(request, 'appTwo/users.html')
