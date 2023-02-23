from django.contrib import admin
from .models import Task,User,Role
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userid','name','city']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','tasknum','status','details']
        
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name','role']        