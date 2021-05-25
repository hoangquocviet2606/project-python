from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30, null= True, blank= True)
    dept = models.CharField(max_length=6, null= True, blank= True)
    creat = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.name