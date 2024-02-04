from django.contrib import admin
from ToDoApp_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Task)


# Register your models here.
