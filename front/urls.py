# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  5:28 下午
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *
app_name = 'front'

urlpatterns = [
    path('/editor/', BasicSampleFormView.as_view(), name='editor'),
    path('',index,name='index'),
]
