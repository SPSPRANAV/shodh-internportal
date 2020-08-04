from django.db import models
from loginapp.models import User
from student.models import Applyform
from multiselectfield import MultiSelectField
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

STATUS=(
    ('Not Assigned','NA'),
    ('Ongoing','OG'),
    ('Completed','CP'),

)
DECISION=(
    ('Accepted','Accept'),
    ('Rejected','Reject'),
)

class Project(models.Model):
    proj_name = models.CharField(max_length=200)
    proj_cpi = models.FloatField(default=0.0)
    proj_description = models.TextField(max_length=1000)
    proj_prof = models.ForeignKey(User, on_delete=models.CASCADE)
    proj_dept = MultiSelectField(choices=DEPT_CHOICES)
    proj_status=models.CharField(choices=STATUS,max_length=12,default='Not Assigned')

class Accept(models.Model):
    appl_id= models.IntegerField()
    value=models.CharField(choices=DECISION,max_length=8,default='Rejected')
    seen=models.BooleanField(default=False)
    def __str__(self):
        return str(self.appl_id) + str(self.value) + str(self.seen)