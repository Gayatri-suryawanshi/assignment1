from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def cse(request):
    return HttpResponse("welcome on cse page")
def etc(request):
    return HttpResponse("welcome on ETC page")
def mech(request):
    return HttpResponse("welcome on MECHANICAL page")
def civil(request):
    return HttpResponse("welcome on CIVIL page")