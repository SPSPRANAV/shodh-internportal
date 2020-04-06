from django.shortcuts import render
from django.http import HttpResponse
from elprofessor.models import Project
from .models import User_profile
from elprofessor.models import Accept
from .models import Applyform
from django.views.generic import CreateView
from .forms import ApplyForm
from loginapp.models import  Student
from loginapp.models import User
from loginapp import models as loginapp_models
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def profile(request):
    local_user = request.user
    context={'username':local_user.username,'email':local_user.email}
    obj1=Student.objects.get(user=local_user)
    context['roll_no']=obj1.roll_no
    context['department'] = obj1.department
    context['student_name'] = obj1.student_name
    context['cpi'] = obj1.cpi
    return render(request, 'student/profile.html',context)

def display(request):
    return render(request,'student/applyform.html')

def errorpage(request):
    return  render(request,'student/errorpage.html')

def index(request):
    list = Project.objects.all()
    context = {'list': list ,}
    return render(request, 'student/index.html', context)
def apply(request):
        local_user = request.user
        l = Student.objects.all()
        x = None
        slist=[]
        for i in l:
            if i.user == local_user:
                x = i.cpi
        base_cpi = x
        list = Project.objects.all()
        for j in list:
            if i.department in j.proj_dept:
                if j.proj_cpi <= base_cpi:
                    slist.append(j)
        context = {'slist': slist ,}
        return render(request, 'student/apply.html',context)
def submitform(request):
    global form_class
    apply_user = request.user
    l = Student.objects.all()
    print("Working")
    if request.method == 'POST':
        print("W2")
        form = ApplyForm(data=request.POST)
        if form.is_valid():
            print("W3")
            x = None
            for i in l:
                if i.user == apply_user:
                    x = i.cpi
            base_cpi = x
            slist = Project.objects.filter(proj_cpi__lte=base_cpi)
            for i in l:
                if i.user == apply_user:
                    if i.roll_no>0 :
                        a = Applyform(name=i.student_name, dept=i.department, cpi=i.cpi,
                                      roll_no=i.roll_no, email=apply_user.email,cv=form.cleaned_data.get('cv'),bio=form.cleaned_data.get('bio'),proj_id=form.cleaned_data.get('proj_id'))
                        flag=0

                        for i in slist:
                            if i.id == a.proj_id:
                                flag=1
                        if flag == 1:
                            a.save()
                            y = a.pk
                            print(a.pk)
                            b = Accept(appl_id=y, value='Rejected', seen=False)
                            subject="New student application for project id {}".format(a.proj_id)
                            message="Respected Professor,Please do look into the new application you have got through the website"
                            from_email='spspranav3@gmail.com'
                            ist=Project.objects.get(id=a.proj_id)
                            prof=ist.proj_prof
                            st=User.objects.get(username=prof)
                            to_email=st.email
                            print(to_email)
                            try:
                                send_mail(subject, message, from_email, [to_email])
                            except BadHeaderError:
                                return HttpResponse('Invalid header found.')

                            b.save()
                            return index(request)
                        else:
                            return errorpage(request)
    else:
        form_class = ApplyForm
        print("W4")
        return render(request, 'student/applyform.html', {'form': form_class})

def my_applications(request):
    local_user = request.user
    l=Applyform.objects.all()
    list=Student.objects.all()
    fist=Accept.objects.all()
    rist=Project.objects.all()
    x=None
    dlist=[]
    plist=[]
    for i in list:
        if i.user == local_user:
            x =i.roll_no
    for j in l:
        if j.roll_no == x:
            for k in fist:
                if k.appl_id == j.id:
                    dlist.append(k)
                    for p in rist:
                        if p.id==j.proj_id:
                            plist.append(p)


    context = {'dlist': dlist,'plist':plist, }
    return render(request, 'student/my_applications.html', context)