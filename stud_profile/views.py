from django.shortcuts import render
from django.db import models
from .models import student
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory

# Create your views here.

from .forms import UpdateProfile


def userdetails(request):
    global form_class
    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'display.html', {'form':form})



    else:
        form_class = UpdateProfile

    return render(request, 'userdetails.html', {
        'form': form_class,
    })