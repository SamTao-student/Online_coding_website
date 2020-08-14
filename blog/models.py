from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100,default=None)
    context = models.TextField()
    author = models.CharField(max_length=10)
    c_time = models.DateTimeField(auto_now_add=True)
    zan_num = models.IntegerField()
    class_choice = models.CharField(max_length = 10,choices=(
        ('yes', '是'),
        ('no', '否'),
    ))
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['c_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'
