import json
from django.shortcuts import render

# Create your views here.
# coding=utf-8

from django.http import HttpResponse,JsonResponse
import datetime
from arp.models import person



def add(request):
    a = request.POST['a']
    b = request.POST['b']
    c = person.objects.get_or_create(name=a,age=int(b))
    return  HttpResponse(str(c))
def chaxun(request):
    allpersernlist = []
    for i in person.objects.all():
        dic ={'name':i.name,'age':i.age}
        allpersernlist.append(dic)
    print(type(allpersernlist))
    print(allpersernlist)
    return JsonResponse(allpersernlist,safe=False)

def index(request):
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'home.html', {'List': List})
def current_datetime(request):
    # 计算当前日期和时间，并以 datetime.datetime 对象的形式保存为局部变量 now
    person.objects.get_or_create(name="王鹏", age=23)

    for i in person.objects.all():
        print(i.name)
        print(i.age)

    # 构建Html响应，使用now替换占位符%s
    html = "<html><body>It is now %s.</body></html>" % len(person.objects.all())

    # 返回一个包含所生成响应的HttpResponse对象
    return HttpResponse(html)
