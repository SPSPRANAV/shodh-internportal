from django import forms
from loginapp.models import Professor,Student
from django.contrib.auth.models import User
class UserForm_stud(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserForm_prof(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class ProfessorForm(forms.ModelForm):
    class Meta():
        model = Professor
        fields = ('prof_website','prof_name','prof_dept')

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('roll_no','student_name','department', 'cpi', 'skills')

