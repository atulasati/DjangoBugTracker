from django.db import models



class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    
    title = models.CharField(max_length=60)
    status = models.CharField(max_length=100)
    details = models.TextField(max_length=150)
    tasknum = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Role(models.Model):
    
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name
 