# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.views import View
from django.views.decorators.csrf import csrf_protect


# Create your views here.


def register(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
                return render(request,'userprofile/login.html',{'username':user.username})
        else:
            form = UserRegistrationForm()
        return render(request,'userprofile/register.html',{'form':form})
