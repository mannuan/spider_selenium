# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .models import Project
from django.http import HttpResponse
from libs import dianping_spot
import inspect
default_script = inspect.getsource(dianping_spot)

def Index(request):
    project_list = Project.objects.all().order_by('-created_time')
    return render(request, 'spider/index.html', context={'project_list': project_list})

def Status(request):
    status = request.GET['status']
    project_id = request.GET['id']
    project = Project.objects.get(project_id=project_id)
    project.status = status
    project.save()
    return HttpResponse('ok')

def Run(request):
    project_id = request.GET['id']
    project = Project.objects.get(project_id=project_id)
    website = project.website
    region = project.region
    type = project.type
    if website == '大众点评' and type == '景点':
        print default_script
    return HttpResponse('ok')