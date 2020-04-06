from django.shortcuts import render
from .forms import ProjectForm
from .forms import AcceptForm
from .models import Project
from .models import Accept
from student.models import Applyform
from loginapp.models import Professor
from loginapp.models import User

# Create your views here.

def index(request):
    list = Project.objects.all().filter(proj_prof=request.user)
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
                    a=Project(proj_name=form.cleaned_data.get('proj_name'),proj_cpi=form.cleaned_data.get('proj_cpi'),proj_description=form.cleaned_data.get('proj_description'),proj_prof=local_user,proj_dept=form.cleaned_data.get('proj_dept'),proj_status='na')
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

def Acceptapply(request):
    global form_class
    local_user=request.user
    if request.method == 'POST':
        form = AcceptForm(request.POST)
        if form.is_valid():
            form.save()
            list = Accept.objects.all()
            for i in list:
                x=i.appl_id
                yist = Applyform.objects.get(pk=x)
                y = yist.proj_id
                rist=Project.objects.get(pk=y)
                if  rist.proj_prof == local_user :
                    a = Accept(value=form.cleaned_data.get('value'),seen=True)
                    a.save()
            return Applications(request)



    else:
        form_class = AcceptForm

    return render(request, 'accept.html', {
        'form': form_class,
    })