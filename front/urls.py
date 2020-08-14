# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  5:28 下午
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,include
from .views import *
from blog import urls as blog_url
app_name = 'front'

urlpatterns = [
    path('',index,name='index'),
    path('editor/<id>',editor.as_view(), name='editor'),
    path('blog/',include(blog_url))
]
