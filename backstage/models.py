from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=128,null=True)
    descriptions = models.TextField(null=True)
    scripts = models.TextField(null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128,null=False)

    class Meta:
        db_table = "task"  # 定义表名
        verbose_name = '任务'  # 这个verbose_name是在管理后台显示的名称
        verbose_name_plural = '任务'
        ordering = ['c_time']  # 排序

    def __str__(self):
        return self.title