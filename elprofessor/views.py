from django.shortcuts import render, redirect
from .forms import ProjectForm
from .forms import AcceptForm
from .models import Project
from .models import Accept
from student.models import Applyform
from loginapp.models import Professor, Student
from loginapp.models import User

# Create your views here.

def index(request):
    list = Project.objects.all().filter(proj_prof=request.user, proj_status="Not Assigned")
    context = {'list': list, }
    return render(request, 'index_elprofessor.html', context)

def profile(request):
    local_user = request.user
    context={'username':local_user.username,'email':local_user.email}
    obj1=Professor.objects.get(user=local_user)
    context['prof_dept'] = obj1.prof_dept
    context['prof_name'] = obj1.prof_name
    context['prof_website'] = obj1.prof_website
    return render(request, 'profile.html',context)


def AddProject(request):
    global form_class
    local_user=request.user
    l=Professor.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            for i in l:
                if i.user == local_user:
                    a=Project(proj_name=form.cleaned_data.get('proj_name'),proj_cpi=form.cleaned_data.get('proj_cpi'),proj_description=form.cleaned_data.get('proj_description'),proj_prof=local_user,proj_dept=form.cleaned_data.get('proj_dept'),proj_status='Not Assigned')
                    a.save()
                    context={'proj_name':a.proj_name,'proj_cpi':a.proj_cpi,'proj_dept':a.proj_dept,'proj_description':a.proj_description}
                    return render(request, 'success.html', context)



    else:
        form_class = ProjectForm

    return render(request, 'addproj.html', {
        'form': form_class,
    })
def Applications(request):
    local_user=request.user
    list = Accept.objects.all()
    flist=[]
    for i in list:
        x = i.appl_id
        z=i.seen
        print(x)
        yist=Applyform.objects.get(pk=x)
        y=yist.proj_id
        rist = Project.objects.get(pk=y)
        if rist.proj_prof == local_user and z==0:
            print(x)
            flist.append(yist)
    context={'flist': flist, }
    return render(request, 'applications.html', context)

def accept(request, pk):
    objects = Accept.objects.all()
    for obj in objects:
        if obj.appl_id == pk:
            obj.seen = True
            obj.value = 'Accepted'
            print(obj.value)
            obj.save()
    print('application accepted')
    print('application seen')
    return redirect('/prof/applications')

def decline(request, pk):
    objects = Accept.objects.all()
    for obj in objects:
        if obj.appl_id == pk:
            obj.seen = True
            obj.value = 'Rejected'
            print(obj.value)
            obj.save()
    print('application accepted')
    print('application seen')
    return redirect('/prof/applications')

def ongoing(request, id):
    obj = Project.objects.get(pk=id)
    obj.proj_status = 'Ongoing'
    obj.save()
    return redirect('/prof/myprojects')

def completed(request, id):
    obj = Project.objects.get(pk=id)
    obj.proj_status = 'Completed'
    obj.save()
    return redirect('/prof/myprojects')

def my_projects(request):
    local_user = request.user
    l=Project.objects.all()
    notassigned=[]
    ongoing=[]
    completed=[]
    count=0
    for j in l:
        if j.proj_prof == local_user:
            if j.proj_status == "Not Assigned":
                notassigned.append(j)
            elif j.proj_status == "Ongoing":
                ongoing.append(j)
            else:
                completed.append(j)
            count=count+1
    print(count)


    context = {'notassigned':notassigned, 'ongoing':ongoing, 'completed':completed,}
    return render(request, 'my_projects.html', context)

def team(request, id):
    l=Applyform.objects.all()
    list=Student.objects.all()
    fist=Accept.objects.all()
    dlist=[]
    for stud in list:
        is_member = False
        for appl in l:
            if appl.roll_no == stud.roll_no and appl.proj_id == id:
                for stat in fist:
                    if stat.appl_id == appl.id and stat.value == 'Accepted':
                        is_member = True
        if is_member == True:
            dlist.append(stud)


    context = {'dlist': dlist, }
    return render(request, 'team.html', context)