from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^surveys/$', views.surveyindex),
    url(r'^surveys/new/$', views.surveycreate)     # This line has changed!
  ]