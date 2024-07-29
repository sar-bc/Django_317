from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import search_projects, paginate_projects


def projects(request):
    pr, search_query = search_projects(request)
    custom_range, pr = paginate_projects(request, pr, 3)

    context = {
        'projects': pr,
        'search_query': search_query,
        # 'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ReviewForm()
    return render(request, "projects/single-project.html", {'project': project_obj, "form": form})


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {"form": form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {"form": form, "project": project}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('account')

    context = {'object': project}
    return render(request, 'projects/delete.html', context)
