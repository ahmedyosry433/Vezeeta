from django.forms import fields
from .models import Blog
from django import forms


class AddPost (forms.ModelForm):
    class Meta :
        
        model =Blog
        fields =('title', 'img', 'description')