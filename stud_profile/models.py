from django.db import models

# Create your models here.
class student(models.Model):
    roll_no=models.IntegerField()
    department=models.CharField(max_length=5)
    student_name=models.CharField(max_length=100)
    cpi=models.FloatField()
    skills=models.TextField(max_length=100)

    def __str__(self):
        return self.student_name + '-' + self.department + '  Department'