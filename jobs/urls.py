from django.conf.urls import url
from jobs.views import *


app_name ='jobs'

urlpatterns=[
   url(r"^post_job/$",post_job, name="postjob"),
   url(r"^alljobs/$",get_alljobs, name="alljobs"),
   url(r'^search_jobs$',get_searched_job, name="searchjobs"),
   url(r'^job/(\d+)$',get_job, name="job"),
]
