from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
ROLES=(
    ('stud','Student'),
    ('prof','Professor'),
)

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #is_prof=True
    prof_name=models.CharField(max_length=100)
    prof_website=models.URLField(max_length=250)
    prof_dept=models.CharField(choices=DEPT_CHOICES,max_length=3)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #is_prof=False
    roll_no=models.IntegerField()
    department=models.CharField(choices=DEPT_CHOICES,max_length=5)
    student_name=models.CharField(max_length=100)
    cpi=models.FloatField()
    #skills=models.CharField(max_length=100)


"""class UserProfileInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_role=models.CharField(max_length=9,choices=ROLES,default='stud')
    user_dept=models.CharField(max_length=25,choices=DEPT_CHOICES)
    user_cpi=models.FloatField(max_length=4)
    user_roll_no=models.IntegerField()
    user_profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username"""
