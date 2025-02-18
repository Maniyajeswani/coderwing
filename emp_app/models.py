from django.db import models

# Create your models here.



class Employees(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)
