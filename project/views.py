from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from jobs.models import *
import requests


class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
         response = requests.get('https://newsapi.org/v2/top-headlines?sources=google-news-in,reuters&apiKey='+settings.NEWS_API_KEY)
         jobs = JobsData.objects.all()
         headlines_data = response.json()
         return render(request,self.template_name,{'headlines_data':headlines_data,'jobs':jobs});
