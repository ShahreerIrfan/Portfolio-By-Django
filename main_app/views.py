
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import Profile
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
def home(request):
    return render(request,"index.html")

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def resume(request):
    return redirect('/path/to/your/resume.pdf')




def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

from django.shortcuts import render
from .models import Project

def project_list(request):
    category = request.GET.get('category')
    if category:
        projects = Project.objects.filter(category=category)
    else:
        projects = Project.objects.all()
    
    context = {'projects': projects}
    
    if not projects and not category:
        context['no_projects_message'] = "No available projects."
    elif not projects and category:
        context['no_projects_message'] = f"No available projects in the {category} category."
    
    return render(request, 'project_list.html', context)


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})




def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    return render(request, 'profile.html', {'profile': profile})