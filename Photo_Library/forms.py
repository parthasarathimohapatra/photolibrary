from django import forms
from .models import *


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']