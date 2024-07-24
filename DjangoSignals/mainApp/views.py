from django.shortcuts import render,HttpResponse


# Create your views here.

# For the exception request
def home(request):
    a=10/0
    return HttpResponse('hello')
