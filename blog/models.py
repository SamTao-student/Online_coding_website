from django.db import models

from mdeditor.fields import MDTextField

class Blog(models.Model):
    title = models.CharField(max_length=100,default=None)
    description = models.TextField()
    content = MDTextField()  # form 表单中定义的MD文本类型
    author = models.CharField(max_length=10)
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')


    read_count = models.IntegerField(default=0, verbose_name='阅读次数')
    zan_num = models.IntegerField(default=0,verbose_name='点赞次数')
    comment_count = models.IntegerField(default=0, verbose_name='评论次数')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['publish_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'

class Comment(models.Model):
    content = MDTextField()
    author = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now_add=True)