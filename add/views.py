from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def add(request,a,b):

    c = int(a)+int(b)
    return HttpResponse(str(c))
