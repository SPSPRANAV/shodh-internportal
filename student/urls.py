from django.urls import path,include
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
from .models import Intern_Model


app_name= 'student'

urlpatterns = [
    path('', views.index , name='index'),
    path('', include('stud_profile.urls')),
    path('apply', views.apply , name='apply'),
    path('profile', views.profile , name='profile'),
    path('displayform',views.display,name='displayform'),
    path('errorpage', views.errorpage, name='errorpage'),
    path('my_applications', views.my_applications, name='my_applications'),
    url(r'submitform/$', views.submitform,name='submitform'),

]
