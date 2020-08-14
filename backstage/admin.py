from django.contrib import admin
from . import models

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','author','c_time')
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name',)
admin.site.register(models.Task,TaskAdmin)
admin.site.register(models.Class,ClassAdmin)

