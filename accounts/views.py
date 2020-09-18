from django.shortcuts import render
from .models import *
import itertools
from django.views import generic

def profile_detail_view(request):
    obj = Image.objects.filter(user__name='Peter Yamamoto')
    context = {
        'album' : obj.values()
    }
    print(obj)
    return render(request, "accounts/profile_detail.html", context)
