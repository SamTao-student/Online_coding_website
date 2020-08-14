# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  9:49 下午
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', blog_index, name='index'),
]