from django.shortcuts import render
from django.views.generic import View
from .forms import *
def index(request):
    if request.method == 'POST':
        task_form = CreateTask(request.POST)
    task_form = CreateTask()
    return render(request,'list.html',locals())