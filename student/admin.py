from django.contrib import admin
from .models import Intern_Model
from .models import User_profile
from .models import  Applyform
# Register your models here.
admin.site.register(Intern_Model)
admin.site.register(User_profile)
admin.site.register(Applyform)
