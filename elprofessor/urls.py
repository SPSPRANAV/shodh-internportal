from django.conf.urls import url
from django.urls import path
from elprofessor import views
from django.views.generic import TemplateView
from .models import Project

app_name = 'elprofessor'

urlpatterns = [
    path('', views.index , name='index1'),
    path('addproj', views.AddProject, name='add'),
    path('display', views.AddProject, name='display'),
    path('applications', views.Applications, name='applications'),
    path('profile', views.profile, name='profile'),
    path('myprojects', views.my_projects, name='myprojects'),
    path('applications/accept/<int:pk>/', views.accept, name='accept'),
    path('applications/decline/<int:pk>/', views.decline, name='decline'),
    path('ongoing/<int:id>/', views.ongoing, name='ongoing'),
    path('completed/<int:id>/', views.completed, name='completed'),
    path('team/<int:id>/', views.team, name='team'),
]
