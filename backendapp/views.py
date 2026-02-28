from django.shortcuts import render
from .faedfa import *

# Create your views here.

def Index(request):

    return render(request,"Index.html")