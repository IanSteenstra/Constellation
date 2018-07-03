from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def index(request):
	
	return render(request, 'home/index.html')

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