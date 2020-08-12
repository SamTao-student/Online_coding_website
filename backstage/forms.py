# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  3:07 下午
# @File    : forms.py
# @Software: PyCharm
from django import forms
from djangocodemirror.fields import CodeMirrorField
from djangocodemirror import widgets
class CreateTask(forms.Form):
    title = forms.CharField()
    descriptions = forms.CharField()
    scripts = CodeMirrorField(label="代码", required=True,
                          config_name="x-c",)
