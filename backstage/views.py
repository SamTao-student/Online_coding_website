from django.shortcuts import render,redirect
from .models import *
from .forms import *
from login.models import *
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
                success = '发布成功！请到任务管理界面查看'
                new_task = Task.objects.create()
                new_task.author = request.session.get('user_name')
                new_task.title = title
                new_task.descriptions = descriptions
                new_task.scripts = scripts
                new_task.save()
                return render(request,'create_task.html',locals())
    task_form = CreateTask()
    return render(request,'create_task.html',locals())

def task_control(request):
    task_list =  Task.objects.filter(author=request.session.get('user_name'))
    return render(request,'task_control.html',locals())

def task_detial(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        remake_task = CreateTask(request.POST)
        if remake_task.is_valid():
            re_title = remake_task.cleaned_data['title']
            print(re_title)
            re_descriptions = remake_task.cleaned_data['descriptions']
            re_scripts = remake_task.cleaned_data['scripts']
            same_title = Task.objects.filter(title=re_title)
            if same_title:
                message = '相同的标题已存在，请重新输入'
                detial_form = EditorTask(initial={'title': task.title,
                                                  'descriptions': task.descriptions,
                                                  'scripts': task.scripts})
                return render(request,'task_detial.html',locals())
            else:
                success = '修改成功'
                task.title = re_title
                task.descriptions = re_descriptions
                task.scripts = re_scripts
                task.save()
                return render(request,'task_detial.html',locals())
    detial_form = EditorTask(initial={'title':task.title,
                                      'descriptions':task.descriptions,
                                      'scripts':task.scripts})
    return render(request,'task_detial.html',locals())

def task_delate(request,id):
    if request.method == 'POST':
        message = '删除成功,请返回任务列表查看'
        task = Task.objects.get(pk=id)
        task.delete()
    return render(request,'delate_task.html',locals())


def class_control(request):
    class_list = Class.objects.filter(create_teacher = request.session.get('user_name'))
    try:
        del request.session['class_id']
    except :
        pass
    return render(request,'class_control.html',locals())

def class_detial(request,id):
    request.session['class_id'] = id
    student_list = Student.objects.filter(to_class=Class.objects.get(pk=id))
    return render(request,'class_detial.html',locals())

def add_student(request):
    if request.method == 'POST':
        add_form = Add_student(request.POST)
        if add_form.is_valid():
            new_class_student = add_form.cleaned_data['student_name']
            try:
                target_student = Student.objects.get(name=new_class_student)
                if target_student.to_class != None:
                    fail_message = '学生已有班级，增加失败!'
                else:
                    success_message = '添加成功'
                    target_student.to_class = Class.objects.get(pk=request.session['class_id'])
                    target_student.save()
            except :
                warning = '学生不存在，添加失败！'
    add_form = Add_student()
    return render(request,'add_student.html',locals())