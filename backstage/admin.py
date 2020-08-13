from django.contrib import admin
from . import models

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','author','c_time')

admin.site.register(models.Task,TaskAdmin)

