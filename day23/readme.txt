
model work

class Department(models.Model) :
    name = models.CharField('Department Name',max_length =40)


project e  

terminal---- 

py .\manage.py makemigrations     # 0001.py file create 
 after migrate a py file create 
 then
  py .\manage.py migrate    #migration to table create
   create user
    terminal- py manage.py createsuperuser

then cheak admin panal

=====================================================
apps to admin.py 
from myapp.models import Department(class name)
below
admin.site.register(Department)

admin panal e add some
to model
def __str__(self) :
        return self.name
    



