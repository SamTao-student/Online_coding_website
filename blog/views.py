from django.shortcuts import render,redirect
from .models import *

import markdown
from .forms import *
from django.db.models import Max
def blog_index(request):
    request.session['current_url'] = 'blog'
    blog_list = Blog.objects.all()
    max_num_blog_dic = Blog.objects.all().aggregate(Max('zan_num'))
    return render(request, 'blog_index.html',locals())
def article_pub(request):
    request.session['current_url'] = 'blog_editor'
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.instance.author = request.session['user_name']
            form.save()
            return redirect('front:blog:index')
    else:
        form = CreateArticleForm()
    return render(request,'article_pub.html',{'form':form})
from markdown.treeprocessors import Treeprocessor


class BootstrapTreeprocessor(Treeprocessor):
    """
    """

    def run(self, node):
        for child in node.getiterator():
            # 如果是 table
            if child.tag == 'table':
                child.set("class", "table table-bordered table-dark")
            elif child.tag == 'h2':
                child.set("class", "h5 text-secondary mb-4")
            # elif child.tag == 'img':
            #    child.set("class","img-fluid")
        return node


class BootStrapExtension(markdown.extensions.Extension):
    """
    """

    def extendMarkdown(self, md):
        """
        """
        md.registerExtension(self)
        self.processor = BootstrapTreeprocessor()
        self.processor.md = md
        self.processor.config = self.getConfigs()
        md.treeprocessors.add('bootstrap', self.processor, '_end')

def blog_detail(request, pk):
    blog = Blog.objects.get(pk = pk)
    blog.content = markdown.markdown(blog.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.tables',
        BootStrapExtension(),
        'markdown.extensions.meta',
        'markdown.extensions.wikilinks',
    ])
    form = CreateCommentForm()
    comments = Comment.objects.all()
    for comment in comments:
        comment.content = markdown.markdown(comment.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables',
            BootStrapExtension(),
            'markdown.extensions.meta',
            'markdown.extensions.wikilinks',
        ])
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.session['user_name']
            form.save()
    return render(request,'blog_detial.html',locals())