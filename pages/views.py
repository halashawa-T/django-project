from django.shortcuts import render

x = {'name' : 'hala taleb' , 'ID': 220221268 , 'address' : 'Cairo' , 'department': 'web developement' , 'email': ''}

def index(request):
    return  render(request , 'pages/index.html', x)