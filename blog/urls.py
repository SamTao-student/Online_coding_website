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
    path('pub/',article_pub,name='pub_article'),
    path('detial/<pk>',blog_detail,name='detial'),
    path('backstage/',blog_control,name='back'),
]