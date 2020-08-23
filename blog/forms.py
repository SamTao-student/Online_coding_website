# -*- coding: utf-8 -*-
# @Author  : Mr.Xia
# @time    :  11:21 下午
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import *

class  CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content',)
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)