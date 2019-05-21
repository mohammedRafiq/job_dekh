from django.conf.urls import url
from django.contrib.auth import views as auth_views
from userprofile.views import *

app_name = 'userprofile'

urlpatterns = [
    url(r"^registration/$", register, name="registration"),
    url(r'^logout/$', auth_views.logout, {'template_name':'userprofile/logout.html'},name='logout'),
    url(r'^login/$', auth_views.login, {'template_name':'userprofile/login.html'},name="login"),
]
