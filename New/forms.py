from django import forms
from .models import Task,User,Role

class AddTaskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields =("title","tasknum","status","details")
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'tasknum' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.TextInput(attrs={'class':'form-control'}),
            'details':  forms.TextInput(attrs={'class':'form-control'})
            
        }

class AddUserForm(forms.ModelForm):
    class Meta :
        model = User
        fields =("userid","name","city")
        widgets = {
            'userid' : forms.NumberInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'city':  forms.TextInput(attrs={'class':'form-control'})
            
        } 

class AddRoleForm(forms.ModelForm):
    class Meta :
        model = Role
        fields =("name","role")
        widgets = {
        
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'role':  forms.TextInput(attrs={'class':'form-control'})
            
        } 