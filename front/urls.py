# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  5:28 下午
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,re_path
from .views import *

app_name = 'front'

urlpatterns = [
    path('',index,name='index'),
    path('editor/<id>',editor.as_view(), name='editor'),
    path('blog/',blog,name='blog'),
]
