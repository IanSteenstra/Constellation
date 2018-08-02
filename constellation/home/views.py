from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project, Applicant
from datetime import datetime
from django.http import HttpResponse as HR


def index(request):
    projects = Project.objects.order_by('project_name')
    context = {'projects' : projects}

    return render(request, 'home/index.html', context)

def new_prod(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            new_project = Project(name=request.user, project_name=request.POST['project_name'], created_dt=datetime.now(), min_gpa=request.POST['min_gpa'], min_year=request.POST['min_year'],
            	min_exp=request.POST['min_exp'], kwords=request.POST['kwords'], req_classes=request.POST['req_classes'])
            new_project.save()
            return redirect('index')

    else:
        form = ProjectForm()

    context = {'form' : form}
    return render(request, 'home/new_prod.html', context)

def apply(request, name, prod, created_dt):
    
    project = Project.objects.get(name=name, project_name=prod, created_dt=created_dt)
    try:
        new_app = Applicant.objects.filter(name=request.user, project=project, score=10)
        if new_app:
            html = "<html><body>Already Applied!</body></html>"
            return HR(html)
        new_app = Applicant.objects.create(name=request.user, project=project, score=10)
        new_app.save()
    except ValueError:
        html = "<html><body>Must sign in before applying to projects!</body></html>"
        return HR(html)

    return redirect('index')