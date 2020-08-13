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
    path('create_task/',create_task,name='create_task'),
    path('task_control/',task_control,name='task_control'),
    path('task_control/detial/<id>',task_detial,name='detial'),
    path('task_control/delate/<id>',task_delate,name='delate'),
    path('class_control/',class_control,name='class_control'),
]