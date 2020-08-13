# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  2:32 下午
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,include
from .views import *
app_name = 'backstage'
urlpatterns = [
    path('',index,name='index'),
    path('create_task/',create_task,name='create_task')
]