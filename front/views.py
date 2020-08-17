from django.shortcuts import render,redirect

from django.views.generic.edit import FormView
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse

from .forms import SampleForm
from backstage import models as bm
import os

def bianyi(form):
    os.popen('touch scripts/test.c', 'w')
    f = open('scripts/test.c', 'w')
    f.write(form.cleaned_data['editor'])
    f.close()
    b = os.popen('gcc scripts/test.c;./a.out')
    c = b.read()
    b.close()
    os.system('rm a.out;rm scripts/test.c')
    return c
class editor(FormView):
    template_name = 'form.html'
    form_class = SampleForm
    initial = {'editor':'''# include <stdio.h>
int main(void)
{
  printf("Hello World");
}'''}
    def get(self, request, *args, **kwargs):
        self.extra_context = {'task': bm.Task.objects.get(pk=kwargs['id']),
                         'result': '您的结果将会显示在这...'}
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = SampleForm(request.POST)
        if form.is_valid():
            self.extra_context = {'task': bm.Task.objects.get(pk=kwargs['id']),
                                'result':bianyi(form)}
        return self.render_to_response(self.get_context_data())

def index(request):
    request.session['current_url'] = 'index'
    task_list = bm.Task.objects.all()
    return render(request,'index.html',locals())




