from django.shortcuts import render,redirect
from .forms import *
from .models import *
import hashlib

def hash_code(s,salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest


def login(request):
    request.session['current_url'] = 'index'
    print(request.session['current_url'])
    if request.session.get('is_login',None):
        return redirect('front:index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = Student.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['user_status'] = user.status
                    return redirect('front:index')
                else:
                    message = "密码不正确！"
            except:
                try:
                    user = Teacher.objects.get(name=username)
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        request.session['user_status'] = user.status
                        return redirect('front:index')
                    else:
                        message = "密码不正确！"
                except :
                    message = "用户不存在！"
                message = "用户不存在！"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("front:index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            status = register_form.cleaned_data['status']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                if Student.objects.filter(name=username) or Teacher.objects.filter(name=username):  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                if Student.objects.filter(email=email) or Teacher.objects.filter(email=email):  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户
                print(status)
                if status == 'student':
                    new_user = Student.objects.create()
                else:
                    new_user = Teacher.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('front:index')
    request.session.flush()
    return redirect('front:index')