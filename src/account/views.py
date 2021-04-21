from typing import Reversible
from django.contrib.auth import authenticate, login
from django.db.models.expressions import F
from django.http.response import HttpResponseRedirect
from account.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form, UpdateUserForm, UserCreationForms, UpdateProfileForm 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.



## All Doctors And Search
@login_required()
def doctors_list(request):
    qeryset = Profile.objects.all().exclude(user_id=request.user.id)
    if request.GET.get('name'):
        qeryset = Profile.objects.filter(name__icontains=request.GET.get('name')).exclude(user_id=request.user.id)
    if request.GET.get('spclized'):
        qeryset = Profile.objects.filter(doctor__icontains=request.GET.get('spclized')).exclude(user_id=request.user.id)
    if request.GET.get('adress'):
        qeryset = Profile.objects.filter(adresss__icontains=request.GET.get('adress')).exclude(user_id=request.user.id)
    context = {
        'doctors': qeryset
    }        
    return render(request, 'user/doctors_list.html', context)

############################################################################################




def user_login(request):

    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('account:doctors_list')

    else:
        form = Login_Form()

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


#############################################################################################

def myprofile(request):

    return render(request, 'user/myprofile.html')

###############################################################################################


def update_profile(request):

    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:

            user_form.save()
            profile_form.save()

            return redirect('account:doctors_list')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/update_profile.html', context)

###############################################################################


def signup(request):
    if request.method == 'POST':
        form  = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_pass)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
           
            return redirect('account:doctors_list')
    else:
        form = UserCreationForms()

    context = {
        'form1': form
    }
    return render(request, 'user/signup.html', context)
#####################################################################


def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug=slug)
    context = {
        'doctors_detail': doctors_detail
    }
    return render(request, 'user/doctors_detail.html', context)
