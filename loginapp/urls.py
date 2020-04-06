from django.conf.urls import url
from loginapp import views
# SET THE NAMESPACE!
app_name = 'loginapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register_stud/$',views.register_stud,name='register_stud'),
    url(r'^register_prof/$', views.register_prof, name='register_prof'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
