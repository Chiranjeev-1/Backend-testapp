from django.shortcuts import render
from .Templates import *

# Create your views here.

def Index(request):

    return render(request,"Index.html")