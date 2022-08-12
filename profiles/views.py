from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from profiles.forms import ProfileForm
from profiles.models import Profile


@require_GET
def index(request):
    return render(request, 'profiles/index.html', {
        'profiles': Profile.objects.all()
    })


@require_GET
def edit(request, uuid):
    profile = Profile.objects.get(id=uuid)
    form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit.html', {
        'profile': profile,
        'form': form
    })


@require_POST
def update(request, uuid):
    profile = Profile.objects.get(id=uuid)
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
    return redirect('home')
