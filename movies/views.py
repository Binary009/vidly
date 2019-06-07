from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP request object is passed to this function
def index(request):
    return HttpResponse("Hello Samuel, Welcome!!")