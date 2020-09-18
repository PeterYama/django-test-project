from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def profile_view(request, *args, **kwars):
    profile_context = {
        "user_name": "Peter",
        "user_sur_name": "Yamamoto",
        "user_nick_name": "Pete",
        "my_number": "0405 944 748 ",
        'user_album': ['user_Picture_1',
                       'user_Picture_2', 'user_Picture_3', 'user_Picture_4', ]
    }
    return render(request, "profile.html", profile_context)
