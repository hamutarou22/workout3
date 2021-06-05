from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Event, Content
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def index(request):

    if request.POST.get("input")=="1":
       a = request.POST.get("delete_pk")
       print(a)
       object_list = Content.objects.filter(id = request.POST.get("delete_pk")).delete()
       object_list = Content.objects.order_by('-training_date')[:10]
       return render(request, 'index.html', {'object_list':object_list})


    object_list = Content.objects.order_by('-training_date')[:10]
    return render(request, 'index.html', {'object_list':object_list})

def neweventfunc(request):
    object_list = Event.objects.all
    return render(request, 'new_event.html', {'object_list':object_list})

def neweventfunc2(request):
    if request.POST.get("add")=="1":
        event = request.POST.get("newevent")
        b = Event(event_name = event)
        b.save()
    
    if request.POST.get("delete")=="1":
       instance =  Event.objects.get(id=request.POST.get("delete_pk"))
       instance.delete()
    
    object_list = Event.objects.all
    return render(request, 'new_event.html', {'object_list':object_list})

def recordfunc(request):
    if request.POST.get("input")=="1":
        event1 = request.POST.get("Event2")
        weight1 = request.POST.get("weight")
        setnumber1 = request.POST.get("setnumber2")
        b = Content(event=event1, weight=weight1, set_number=setnumber1)
        b.save()
        object_list = Content.objects.order_by('-training_date')
        return render(request, 'index.html', {'object_list':object_list})

    object_list = Event.objects.all
    return render(request, 'record.html', {'object_list':object_list})

def changefunc(request):
    response = "Hello, world. You're at the change."
    return HttpResponse(response)



def tablefunc(request):

    if  request.POST.get("input")=="1":
        input2 = "2"
        NumberOfRecord = request.POST.get("number_record")
        result_list = Content.objects.filter(event=request.POST.get("Event2")).order_by('-training_date')[:int(NumberOfRecord)]
        event_list = Event.objects.all
        return render(request, 'make_table.html', {'result_list':result_list, 'event_list':event_list ,"input2":input2 }) 

    else:
        input2 = "1"
        result_list = Content.objects.order_by('-training_date')
        event_list = Event.objects.all
        return render(request, 'make_table.html', {'result_list':result_list, 'event_list':event_list ,"input2":input2 })


