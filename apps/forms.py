#from django import forms
from .models import ImageFile
from django.forms import ModelForm

class ImageFileForm(ModelForm):
    class Meta:
        model = ImageFile
        fields = ['data', 'detection', 'maxResult']
