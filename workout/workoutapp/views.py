from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Content
# Create your views here.


def index(request):
    object_list = Content.objects.order_by('training_date')[:5]
    return render(request, 'index.html', {'object_list':object_list})

def neweventfunc(request):
    response = "Hello, world. You're at the new event."
    return HttpResponse(response)

def recordfunc(request):
    object_list = Event.objects.all
    return render(request, 'record.html', {'object_list':object_list})

def changefunc(request, pk):
    response = "Hello, world. You're at the change %s."
    return HttpResponse(response % pk)
    
def tablefunc(request):
    response = "Hello, world. You're at the table."
    return HttpResponse(response)
