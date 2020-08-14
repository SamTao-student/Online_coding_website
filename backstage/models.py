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
        verbose_name_plural = '任务' #复数形式的显示名称
        ordering = ['c_time']  # 排序

    def __str__(self):
        return self.title
class Class(models.Model):
    class_name = models.CharField(max_length=20)
    max_student = models.IntegerField()
    create_teacher = models.CharField(max_length=10,default=None)
    class Meta:
        db_table = "class"  # 定义表名
        verbose_name = '班级'  # 这个verbose_name是在管理后台显示的名称
        verbose_name_plural = '班级' #复数形式的显示名称

    def __str__(self):
        return self.class_name