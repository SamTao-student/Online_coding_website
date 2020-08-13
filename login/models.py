from django.db import models
from backstage import models as bm

class Student(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    to_class = models.ForeignKey(bm.Class,on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=10,editable=False,default='学生')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '学生'
        verbose_name_plural = '学生'
class Teacher(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,editable=False, default='老师')
    own_class = models.ManyToManyField(bm.Class)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '老师'
        verbose_name_plural = '老师'
