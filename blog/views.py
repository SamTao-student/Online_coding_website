from django.shortcuts import render
from .models import Blog
from django.db.models import Max
def blog_index(request):
    blog_list = Blog.objects.all()
    max_num_blog_dic = Blog.objects.all().aggregate(Max('zan_num'))
    max_num_blog = Blog.objects.get(zan_num=max_num_blog_dic['zan_num__max'])
    return render(request, 'blog_index.html',locals())
