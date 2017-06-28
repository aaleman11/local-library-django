#Linking to locallibrary/urls.py file

#This is where we'll add our patterns as we build the application

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index')       #Will call views.index is pattern is detected
]