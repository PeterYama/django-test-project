from django.shortcuts import render
from .models import *
import itertools
from django.views import generic

class ProfileView(generic.ListView):
    model = Profile
    def get_queryset(self):
        return Profile.objects.filter(id=1)[:5]

    # obj = Image.objects.filter(user__name='Peter Yamamoto')
    # context = {
    #     'album' : obj.values()[0]
    # }
    # print(obj.values()[0])
    # return render(request, "accounts/detail.html", context)
