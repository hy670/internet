"""internet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url
from arp.views import current_datetime, index, add, chaxun, person_del
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^time/$', current_datetime),
    url(r'^chaxun/$', chaxun),
    url(r'^person_del/$', person_del),
    url(r'^$', index),
    url(r'^add/$', add, name='add'),
    url(r'^add/(\d+)/(\d+)', add, name='add'),
    path('admin/', admin.site.urls),
]
