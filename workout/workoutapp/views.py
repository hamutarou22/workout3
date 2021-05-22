from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detailfunc(request, pk):
    response = "Hello, world. You're at the detail %s."
    return HttpResponse(response % pk)

def recordfunc(request):
    response = "Hello, world. You're at the record."
    return HttpResponse(response)

def changefunc(request, pk):
    response = "Hello, world. You're at the change %s."
    return HttpResponse(response % pk)
    
def tablefunc(request, pk):
    response = "Hello, world. You're at the table."
    return HttpResponse(response)
