from django import forms
from .models import student


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = student
        fields = ['roll_no', 'department', 'student_name', 'cpi', 'skills']