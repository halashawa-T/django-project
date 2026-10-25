from django.shortcuts import render
from .models import Person

x = {'name' : 'hala taleb' , 'ID': 220221268 , 'address' : 'Cairo' , 'department': 'web developement' , 'email': ''}

def index(request):
    return  render(request , 'pages/index.html', x)

def home(request):
    return render(request, 'pages/homePage.html' , {'por': Person.objects.all()} ) 