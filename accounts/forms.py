from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class RawProfileForm(forms.Form):
    name = forms.CharField()
    bio = forms.CharField()
    address = forms.CharField()
    age = forms.DecimalField()

