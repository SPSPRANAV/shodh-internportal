from django.urls import path
from elprofessor import views
from django.views.generic import TemplateView
from .models import Project

app_name = 'elprofessor'

urlpatterns = [
    path('', views.index , name='index1'),
    path('addproj', views.AddProject, name='add'),
    path('display', views.AddProject, name='display'),
    path('accept',views.Acceptapply,name='accept'),
    path('applications', views.Applications, name='applications'),
    path('profile', views.profile, name='profile'),

]
