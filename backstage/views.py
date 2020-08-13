from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
    return render(request,'list.html')

def create_task(request):
    if request.method == 'POST':
        task_form = CreateTask(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data['title']
            descriptions = task_form.cleaned_data['descriptions']
            scripts = task_form.cleaned_data['scripts']
            same_title = Task.objects.filter(title=title)
            if same_title:
                message = '相同的标题已存在，请重新输入'
                return render(request,'create_task.html',locals())
            else:
                new_task = Task.objects.create()
                new_task.author = request.session.get('user_name')
                new_task.title = title
                new_task.descriptions = descriptions
                new_task.scripts = scripts
                new_task.save()
                return HttpResponse('Success')
        else:
            return HttpResponse('FormUnviald')
    task_form = CreateTask()
    return render(request,'create_task.html',locals())