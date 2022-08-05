from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from projects.models import Project
from .forms import ProjectForm


@require_GET
def index(request):
    return render(request, 'projects/index.html', {
        'projects': Project.objects.all()
    })


@require_GET
def show(request, uuid):
    try:
        project = Project.objects.get(id=uuid)
    except Project.DoesNotExist:
        project = None

    return render(request, 'projects/show.html', {
        'project': project,
    })


@require_GET
def create(request):
    form = ProjectForm()
    return render(request, 'projects/create.html', {
        'form': form
    })


@require_POST
def store(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')


@require_GET
def edit(request, uuid):
    project = Project.objects.get(id=uuid)
    form = ProjectForm(instance=project)
    return render(request, 'projects/edit.html', {
        'project': project,
        'form': form
    })


@require_POST
def update(request, uuid):
    project = Project.objects.get(id=uuid)
    form = ProjectForm(request.POST, instance=project)
    if form.is_valid():
        form.save()
    return redirect('home')


@require_POST
def delete(request, uuid):
    project = Project.objects.get(id=uuid)
    project.delete()
    return redirect('home')
