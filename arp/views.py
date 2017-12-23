# Create your views here.
# coding=utf-8

from django.http import HttpResponse, JsonResponse
from arp.models import person
from django.shortcuts import render


def add(request):
    a = request.POST['a']
    b = request.POST['b']
    c = person.objects.get_or_create(name=a, age=int(b))
    d = c[1]
    return HttpResponse(str(d))


def person_del(request):
    aa = request.POST['aa']
    c = person.objects.filter(id=aa).delete()
    d = c[0]
    return HttpResponse(str(d))


def chaxun(request):
    allpersernlist = []
    for i in person.objects.all().values_list('id','name','age'):
        dic = {'id': i[0], 'name': i[1], 'age': i[2]}
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
