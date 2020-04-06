from django.shortcuts import render
from loginapp.forms import UserForm_stud,UserForm_prof,StudentForm,ProfessorForm
from loginapp.models import Student
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'loginapp/base.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_stud(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm_stud(data=request.POST)
        profile_form = StudentForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm_stud()
        profile_form = StudentForm()
    return render(request,'loginapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def register_prof(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm_prof(data=request.POST)
        profile_form = ProfessorForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm_prof()
        profile_form = ProfessorForm()
    return render(request,'loginapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #user_role=request.POST.get('user_role')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                x=1
                l=Student.objects.all()
                for i in l:
                    if i.user==user:
                        x=0
                        break
                print(x)
                return render(request, 'loginapp/index.html',{'x':x})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'loginapp/base.html', {})
