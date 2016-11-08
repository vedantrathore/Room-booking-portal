"""nsacrbp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bookmyroom.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),
    url(r'login',login,name='login'),
    url(r'signup',signup,name='signup'),
    url(r'book/new/$', book_new,name='book_new'),
    url(r'bookings', my_bookings, name='my_bookings'),
    url(r'book/(?P<pk>\d+)/$', book_detail, name='book_detail'),
    url(r'book/(?P<pk>\d+)/edit/$', book_edit, name='book_edit'),
    url(r'mail/(?P<pk>\d+)/$', mail, name='mail'),
    url(r'logout', logout,name='logout'),
]
