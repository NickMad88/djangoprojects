from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.logins),
    url(r'^users/$', views.users),
    url(r'^users/new/$', views.register)     # This line has changed!
  ]