from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def logins(request):
    return HttpResponse("placeholder for user login")
def users(request):
    return HttpResponse("placeholder to display list of users")