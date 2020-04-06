from django import forms
from .models import Project
from .models import Accept

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('proj_name','proj_cpi','proj_description','proj_dept')
class AcceptForm(forms.ModelForm):
    class Meta():
        model = Accept
        fields = ('value',)
