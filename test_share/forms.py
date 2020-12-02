from django.forms import ModelForm
from django import forms
from .models import Test_Image

class TestImageForm(ModelForm):
    class Meta:
        model = Test_Image
        fields = ['title', 'year', 'image', 'comment']