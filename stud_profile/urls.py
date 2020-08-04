from django.urls import path
from django.contrib import admin

from stud_profile import views as stud_profile_views

urlpatterns = [
    path('userdetails/', stud_profile_views.userdetails),
    path('display/', stud_profile_views.userdetails),

    path('', admin.site.urls),
]