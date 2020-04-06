from django.db import models
from loginapp import models as loginapp_models
from loginapp.models import Student,Professor
from django.contrib.auth.models import User
DEPT_CHOICES=(
    ('CSE','Computer Science and Engineering'),
    ('ECE','Electronics & Commmunication  Engineering'),
    ('EEE','Electrical & Electronics Engineering'),
    ('ME','Mechanical Engineering'),
    ('CST','Chemical Science and Technology'),
    ('CL','Chemical Engineering'),
    ('MNC','Maths and Computing'),
    ('CE','Civil Engineering'),
    ('BT','Bio Technology'),
    ('EP','Engineering Physics'),

)

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    # Main Function


dict_obj = my_dictionary()
l=Professor.objects.all()
for i in l:
    dict_obj.add(i.user.username,i.prof_name)

PROF_CHOICES=dict_obj
# Create your models here.
class Intern_Model(models.Model):
    department_name=models.CharField(choices=DEPT_CHOICES,max_length=5)
    prof_name=models.CharField(max_length=100)
    min_cpi=models.FloatField()
    title=models.CharField(max_length=50)
    skills=models.TextField(max_length=100)
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.prof_name + '-' + self.department_name + '  Department'

class User_profile(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Applyform(models.Model):
    roll_no=models.IntegerField(default=0)
    name=models.CharField(max_length=100,default='asd')
    dept=models.CharField(choices=DEPT_CHOICES,max_length=5,default='cse')
    cpi=models.FloatField(default=0.0)
    email=models.EmailField(default='abc@xyz.com')
    cv=models.URLField(default='ac@bc.com')
    bio = models.TextField(default='wish')
    proj_id=models.IntegerField(default='1')