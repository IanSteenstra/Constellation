from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from home.models import Project
from .models import Experience
from .forms import ExpForm
# Create your views here.

def profile(request):
    user = request.user
    exp_list = []
    prod_list = []
    exps = Experience.objects.filter(name=user)
    prod = Project.objects.filter(name=user)

    for exp in exps:
        exp_list.append(exp)

    for p in prod:
        prod_list.append(p)

    args = {'user': user, 'exps': exp_list, 'prod': prod_list}
    return render(request, 'users/profile.html', args)

def new_exp(request):
    if request.method == 'POST':
        form = ExpForm(request.POST)

        if form.is_valid():
            new_exp = Experience(name=request.user, title=request.POST['title'], company=request.POST['company'], 
                time=request.POST['time'], desc=request.POST['desc'])
            new_exp.save()
            return redirect('profile')

    else:
        form = ExpForm()
    
    args = {'form': form}
    return render(request, 'users/new_exp.html', args)
