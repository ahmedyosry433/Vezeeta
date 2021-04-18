from django.forms import fields

from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class Login_Form(forms.ModelForm):

    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمه المرور', widget=forms.PasswordInput())

    class Meta:

        model = User

        fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):

    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.CharField(label='البريد الالكتروني ')

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'email')


class UserCreationForms(UserCreationForm):

    username = forms.CharField(label='اسم المستخدم')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني ')
    password1 = forms.CharField(label='كلمه المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = ('name', 'subtitle', 'adresss', 'adresss_detail', 'number_phone','working_hours', 'wating_time', 'who_i', 'price', 'img', 'facebook', 'twitter', 'google', 'specialist_doctor')
