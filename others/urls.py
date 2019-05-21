from django.conf.urls import url
from others.views import News

app_name='others'


urlpatterns = [
    url(r"^all_news/$",News.as_view(), name="all_news"),

]
