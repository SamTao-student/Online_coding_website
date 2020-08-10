from django.shortcuts import render

from django.views.generic.edit import FormView
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse

from .forms import SampleForm
import os

class BasicSampleFormView(FormView):
    template_name = 'form.html'
    form_class = SampleForm
    initial = {'editor':'''# include <stdio.h>
int main(void)
{
  printf("Hello World");
}'''}
    def form_valid(self, form):
        os.popen('touch scripts/test.c','w')
        f = open('scripts/test.c','w')
        f.write(form.cleaned_data['editor'])
        f.close()
        b = os.popen('gcc scripts/test.c;./a.out')
        c = b.read()
        print(c)
        b.close()
        os.system('rm a.out')
        return HttpResponse('success')

def index(request):
    return render(request,'base.html')


