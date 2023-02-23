from .views import Home,Add_Task , Delete_Task ,Edit_Task
from .views import Add_User,Delete_User,Edit_User
from .views import Add_Role,Edit_Role,Delete_Role

from django.urls import path

urlpatterns = [
   
    path('', Home.as_view(), name='home'),
    
     
    path('add-task/', Add_Task.as_view(),name='add-task'),
    path('delete-task/', Delete_Task.as_view(),name='delete-task'),
    path('edit-task/<int:id>/', Edit_Task.as_view(),name="edit-task"),
    
    path('add-user/', Add_User.as_view(),name='add-user'),
    path('delete-user/', Delete_User.as_view(),name='delete-user'),
    path('edit-user/<int:id>/', Edit_User.as_view(),name="edit-user"),
    
    path('add-role/', Add_Role.as_view(),name='add-role'),
    path('delete-role/', Delete_Role.as_view(),name='delete-role'),
    path('edit-role/<int:id>/', Edit_Role.as_view(),name="edit-role")
]

