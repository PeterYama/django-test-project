from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import *
import itertools
from django.views import generic
from .forms import ProfileForm, RawProfileForm


def profile_create_view(request):
    form = ProfileForm()
    if request.method =="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # new objects can be created from the cleaned_data
            # Profile.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
        else:
            print("Input is not valid" + form.errors)
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, "accounts/profile_create.html", context)


def profile_detail_view(request, id):
    try:
        obj = Profile.objects.filter(id=id)
    except Profile.DoesNotExist:
        raise Http404
    # obj = get_object_or_404(Profile, id=id)
    context = {
        'Profile': obj
    }
    return render(request, "accounts/profile_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'name' : 'insert your name',
        'bio' : 'talk about your channel',
        'address' : 'only visible to you',
        'profile_image' : 'None',
    }
    obj = Profile.Objects.get(id=1)
    form = ProfileForm(request.POST or None, initial=initial_data,instance=obj)
    if form.is_valid():
        form.save()
        print("Form Edited")
    context = {
        'form': form
    }
    return render(request, "accounts/profile_create.html")
