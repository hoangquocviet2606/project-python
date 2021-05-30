from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    # id = models.AutoField(primary_key=True, default=1000)
    name = models.CharField(max_length=30, null= True, blank= True)
    dept = models.CharField(max_length=6, null= True, blank= True)
    creat = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  



    def __str__(self):
        return self.name