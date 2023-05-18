from django.shortcuts import render,HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Welcome, your Django project has been successfully deployed !")