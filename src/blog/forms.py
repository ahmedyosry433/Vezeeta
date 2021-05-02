from django.forms import fields
from .models import Blog,Comment
from django import forms


class AddPost (forms.ModelForm):
    
    class Meta :
        model =Blog
        fields =('title', 'img', 'description')
        
class CommentForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    body= forms.CharField(widget= forms.TextInput
                        (attrs={'placeholder':'Write Comment'}))
    email= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Email : Example@.com'}))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')