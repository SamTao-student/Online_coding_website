# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  10:22 上午
# @File    : forms.py
# @Software: PyCharm

from django import forms

from djangocodemirror.fields import CodeMirrorField


class SampleForm(forms.Form):
    editor = CodeMirrorField(label="请输入你的代码", required=True,
                          config_name="x-c",)