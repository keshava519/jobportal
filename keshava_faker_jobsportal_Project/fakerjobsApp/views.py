from django.shortcuts import render
from fakerjobsApp.models import *

# Create your views here.
def index(request):
    return render(request,'fakerjobsApp/index.html')


def hydjobsview(request):
    hydjobs_list=Hydjobs.objects.order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render (request,'fakerjobsApp/hydjobs.html',context=my_dict)

def Banglorejobsview(request):
    Banglorejobs_list=Banglorejobs.objects.order_by('date')
    my_dict={'Banglorejobs_list':Banglorejobs_list}
    return render (request,'fakerjobsApp/banglorejobs.html',context=my_dict)

def Chennaijobsview(request):
    chennaijobs_list=Hydjobs.objects.order_by('date')
    my_dict={'chennaijobs_list':chennaijobs_list}
    return render (request,'fakerjobsApp/chennaijobs.html',context=my_dict)

def Punejobsview(request):
    punejobs_list=Hydjobs.objects.order_by('date')
    my_dict={'punejobs_list':punejobs_list}
    return render (request,'fakerjobsApp/punejobs.html',context=my_dict)
