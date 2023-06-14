from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login

from .models import Profile
from .forms import Profileform, Userform, signupform

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home:home')
    else:
        form = signupform
    cont = {'form': form}
    return render(request, 'signup.html', cont)


def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    cont = {'profile': user_profile}
    return render(request, 'profile.html', cont)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = Userform(request.POST, request.FILES, instance=request.user)
        profileform = Profileform(
            request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('users:profile'))
    else:
        userform = Userform(instance=request.user)
        profileform = Profileform(instance=profile)
    return render(request, 'profile_edit.html', {'profileform': profileform, 'userform': userform})
