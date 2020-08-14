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

class EditorTask(forms.Form):
    title = forms.CharField(label='标题')
    descriptions = forms.CharField(widget=forms.Textarea, label='题目描述')
    scripts = forms.CharField(widget=forms.Textarea, label='示例代码')

class EditorClass(forms.Form):
    class_name = forms.CharField(label='班级名称')
    max_student = forms.IntegerField(label='班级最大人数')
class Add_student(forms.Form):
    student_name = forms.CharField(label='学生姓名')
