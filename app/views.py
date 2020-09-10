from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def HomePage(request):
    return render(request,"app/homepage.html") 


def gallery(request):
    images = Image.objects.all()
    return render(request,"app/gallery.html",{'images': images}) 


def books(request):
    return render(request,"app/books.html")