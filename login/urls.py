# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  11:46 下午
# @File    : urls.py
# @Software: PyCharm

from django.urls import path,include
from . import views

app_name = 'login'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout),
    path('test/',views.test),
]