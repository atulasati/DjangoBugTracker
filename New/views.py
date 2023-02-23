from django.shortcuts import render,redirect
from .models import Task , User ,Role
from django.views import View
from .forms import AddTaskForm , AddUserForm, AddRoleForm

class Home(View):
    def get(self, request):
        task_data = Task.objects.all()
        user_data = User.objects.all()
        role_data = Role.objects.all()
        context = {
              'taskdata': task_data,
              'userdata': user_data,
              'roledata': role_data
            }
        return render(request,'new/home.html',context)


"""tASK"""
class Add_Task(View):
    def get(self,request):
        fm = AddTaskForm()
        return render(request,'new/add-task.html',{'form':fm})
    
    
    def post(self,request):
        fm = AddTaskForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
        else:
            return render(request, 'new/add-task.html', {'form':fm})

class Delete_Task(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        taskdata = Task.objects.get(id=id)
        taskdata.delete()
        return redirect('/')
    
class Edit_Task(View):
    def get(self,request,id):
        stu = Task.objects.get(id=id)
        fm = AddTaskForm(instance=stu)
        return render(request,'new/edit-task.html',{'form':fm})
    def post(self,request,id):
        stu = Task.objects.get(id=id)
        fm=AddTaskForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        
        
"""USER DASHBOARD"""        

class Add_User(View):
    def get(self,request):
        fn = AddUserForm()
        return render(request,'new/add-user.html',{'form':fn})
    
    
    def post(self,request):
        fn = AddUserForm(request.POST)
        if fn.is_valid():
            fn.save()
            return redirect("/")
        else:
            return render(request, 'new/add-user.html', {'form':fn})

class Delete_User(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        userdata = User.objects.get(userid=id)
        userdata.delete()
        return redirect('/')
    
class Edit_User(View):
    def get(self,request,id):
        user = User.objects.get(userid=id)
        fn = AddUserForm(instance=user)
        return render(request,'new/edit-user.html',{'form':fn})
    def post(self,request,id):
        user = User.objects.get(userid=id)
        fn=AddUserForm(request.POST,instance=user)
        if fn.is_valid():
            fn.save()
            return redirect('/')
 
    """Role Section"""   

class Add_Role(View):
    def get(self,request):
        fo = AddRoleForm()
        return render(request,'new/add-role.html',{'form':fo})
    
    
    def post(self,request):
        fo = AddRoleForm(request.POST)
        if fo.is_valid():
            fo.save()
            return redirect("/")
        else:
            return render(request, 'new/add-role.html',{'form':fo})

class Delete_Role(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        roledata = Role.objects.get(id=id)
        roledata.delete()
        return redirect('/')
    
class Edit_Role(View):
    def get(self,request,id):
        rol = Role.objects.get(id=id)
        fo = AddRoleForm(instance=rol)
        return render(request,'new/edit-role.html',{'form':fo})
    def post(self,request,id):
        rol = Role.objects.get(id=id)
        fo=AddRoleForm(request.POST,instance=rol)
        if fo.is_valid():
            fo.save()
            return redirect('/')
        
        