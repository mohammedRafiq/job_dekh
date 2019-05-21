# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
import requests

class News(TemplateView):
     template_name = "others/all_news.html"
     def get(self, request, *args, **kwargs):
         response = requests.get('https://newsapi.org/v2/top-headlines?sources=google-news-in,reuters&apiKey='+settings.NEWS_API_KEY)
         headlines_data = response.json()
         return render(request,self.template_name,{'headlines_data':headlines_data})






# Create your views here.
