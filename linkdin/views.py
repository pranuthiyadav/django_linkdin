from django.shortcuts import render
from django.http import HttpResponse

from .models import post

# Create your views here.

def index(request): 

    abc = post.objects.all()

    #print(abc)

    return render(request, 'index.html',context={'abc':abc}) 

def about(request):
    return render(request, 'about.html')