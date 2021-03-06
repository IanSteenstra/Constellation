from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from home.models import Project, Applicant
from .models import Experience
from .forms import ExpForm, UserForm, ProfileForm

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            login(request, new_user)
            return redirect('profile')
    else:
        form = UserForm()

    args = {'form': form}
    return render(request, 'users/new_user.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            old_username = request.user.username
            new_username = request.POST['username']
            user = User.objects.get(username=request.user)
            if new_username != '':
                user.username = new_username
                user.profile.username = new_username
            if request.POST['first_name'] != '':
                user.first_name = request.POST['first_name']
            if request.POST['last_name'] != '':
                user.last_name = request.POST['last_name']
            if request.POST['email'] != '':
                user.email = request.POST['email']
            # user.password=request.POST['password']
            user.save()
            if (request.POST['gpa'] != ''): 
                user.profile.gpa = request.POST['gpa']
            # Make the default year and role whatever was first put in
            if (request.POST['year'] != ''): 
                user.profile.year = request.POST['year']
            if (request.POST['role'] != ''): 
                user.profile.role = request.POST['role']
            if (request.POST['desc'] != ''): 
                user.profile.desc = request.POST['desc']
            if (request.POST['skills'] != ''): 
                user.profile.skills = request.POST['skills']
            if (request.POST['classes'] != ''): 
                user.profile.classes = request.POST['classes']
            user.profile.save()
            prod = Project.objects.filter(name=old_username)
            for p in prod:
                p.name = user.username
                p.save()
            login(request, user)
            return redirect('profile')
    else:
        form = ProfileForm()

    args = {'form': form}
    return render(request, 'users/edit_profile.html', args)

def profile(request):
    user = User.objects.get(username=request.user)
    exps = Experience.objects.filter(name=user)
    prod = Project.objects.filter(name=user)
    app_list = []
    exp_list = []
    prod_list = []
    for exp in exps:
        exp_list.append(exp)
    for p in prod:
        apps = Applicant.objects.filter(project=p)
        for a in apps:
            app_list.append(a)
        prod_list.append(p)
            
    args = {'user': user, 'exps': exp_list, 'prod': prod_list, 'app': app_list}
    return render(request, 'users/profile.html', args)

def new_exp(request):
    if request.method == 'POST':
        form = ExpForm(request.POST)

        # Form isnt valid...FIX
        if form.is_valid():
            new_exp = Experience(name=request.user, title=request.POST['title'], company=request.POST['company'], 
                start_date=request.POST['start_date'], end_date=request.POST['end_date'], desc=request.POST['desc'])
            new_exp.save()
            return redirect('profile')

    else:
        form = ExpForm()
    
    args = {'form': form}
    return render(request, 'users/new_exp.html', args)
