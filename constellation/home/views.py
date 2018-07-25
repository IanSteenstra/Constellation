from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Project
from .forms import ProjectForm


def index(request):
    projects = Project.objects.order_by('project_name')
    context = {'projects' : projects}

    return render(request, 'home/index.html', context)

def new_prod(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            new_project = Project(name=request.POST['name'], project_name=request.POST['project_name'], min_gpa=request.POST['min_gpa'], min_year=request.POST['min_year'],
            	min_exp=request.POST['min_exp'], kwords=request.POST['kwords'], req_classes=request.POST['req_classes'])
            new_project.save()
            return redirect('index')

    else:
        form = ProjectForm()

    context = {'form' : form}
    return render(request, 'home/new_prod.html', context)
