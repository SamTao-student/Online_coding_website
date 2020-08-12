# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  11:46 下午
# @File    : urls.py
# @Software: PyCharm

from django.urls import path,include
from . import views

app_name = 'login'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),
    path('test/',views.test),
]