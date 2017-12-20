# Create your views here.
# coding=utf-8

from django.http import HttpResponse, JsonResponse
from arp.models import person
from django.shortcuts import render


def add(request):
    a = request.POST['a']
    b = request.POST['b']
    c = person.objects.get_or_create(name=a, age=int(b))
    return HttpResponse(str(c))


def chaxun(request):
    allpersernlist = []
    for i in person.objects.all():
        dic = {'name': i.name, 'age': i.age}
        allpersernlist.append(dic)
    return JsonResponse(allpersernlist, safe=False)


def index(request):
    List = map(str, range(100))
    return render(request, 'home.html', {'List': List})


def current_datetime(request):
    person.objects.get_or_create(name="王鹏", age=23)
    for i in person.objects.all():
        print(i.name)
        print(i.age)
    html = "<html><body>It is now %s.</body></html>" % len(person.objects.all())
    return HttpResponse(html)
