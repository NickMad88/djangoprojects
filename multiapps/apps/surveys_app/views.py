from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def surveyindex(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def surveycreate(request):
    return HttpResponse("placeholder for users to add new survey")