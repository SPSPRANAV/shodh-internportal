from django import forms
from .models import Applyform
from .models import User_profile


class ApplyForm(forms.ModelForm):
    class Meta():
        model = Applyform
        fields = ('cv', 'bio', 'proj_id')