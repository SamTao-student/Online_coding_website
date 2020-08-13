# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  3:07 下午
# @File    : forms.py
# @Software: PyCharm
from django import forms


class CreateTask(forms.Form):
    title = forms.CharField(label='标题')
    descriptions = forms.CharField(widget=forms.Textarea,label='题目描述')
    scripts =forms.CharField(widget=forms.Textarea,label='示例代码')


