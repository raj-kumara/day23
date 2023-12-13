from django.db import models
from datetime import datetime
# Create your models here.

class Department(models.Model) :
    name = models.CharField('Department Name',max_length =40)
    
    def __str__(self) :
        return self.name

class Employee(models.Model):
         GENDER_CHOICES=[
            ('Male','Male'),('Female','Female'),('other','other'),
            ]
         name=models.CharField("Employee name", max_length=50)
         email=models.EmailField("Employee Email", max_length=254,unique=True)
         adress=models.TextField('Employee Address', max_length=500)
         phone=models.CharField('Employee Phone',max_length=20)
         doj =models.DateField('Date of joining',default=datetime.now,blank=True)
         salary=models.DecimalField('Salary',max_digits=8,decimal_places=2)
         gender=models.CharField('Gender',max_length=10,choices=GENDER_CHOICES,default='Male')
         photo=models.FileField('Photo',upload_to='employee',default='employee/blank.jpg')
         Department=models.ForeignKey(Department,on_delete=models.CASCADE)
         
         
         def __str__(self):
             return self.name
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    