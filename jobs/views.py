# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import *
from .models import *
from django.views import View
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


def get_job(request,id):
    jobs  = JobsData.objects.filter(id=id)
    return render(request,'jobs/job.html',{'jobs':jobs[0]})

def get_alljobs(request):
    jobs_list = JobsData.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(jobs_list, 2)

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request,'jobs/alljobs.html',{'jobs':jobs})

def get_searched_job(request):

        search_word = request.GET.get('search')
        experience = request.GET.get('exp')
        print(experience)
        jobs_list = JobsData.objects.filter( Q(years_of_experience=experience) & (Q(location__contains=search_word) |
        Q(designation__contains=search_word) | Q(title__contains=search_word)))
        print(jobs_list,"Jobs list")
        page = request.GET.get('page', 1)

        paginator = Paginator(jobs_list, 2)

        try:
          jobs = paginator.page(page)
        except PageNotAnInteger:
          jobs = paginator.page(1)
        except EmptyPage:
          jobs = paginator.page(paginator.num_pages)
        return render(request,'jobs/alljobs.html',{'jobs':jobs})

def post_job(request):
    if request.method == 'POST':
        form = PostJob(request.POST)
        if form.is_valid():
            designation=form.cleaned_data['designation']
            employer=form.cleaned_data['employer']
            years_of_experience=form.cleaned_data['years_of_experience']
            location=form.cleaned_data['location']
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            created=datetime.now()
            print(designation)
            jobs = JobsData.objects.create(designation=designation.replace('(u\'','').replace('\',)',''),
            employer=employer.replace('(u\'','').replace('\',)',''),
            years_of_experience=years_of_experience.replace('(u\'','').replace('\',)',''),
            location=location.replace('(u\'','').replace('\',)',''),
            title=title.replace('(u\'','').replace('\',)',''),
            description=description.replace('(u\'','').replace('\',)',''))

            return render(request,'jobs/post_job.html',{'job_employer':employer.replace('(u\'','').replace('\',)',''),'form':form})
    else:
        form = PostJob()
    return render(request,'jobs/post_job.html',{'form':form})
