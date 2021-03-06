# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, "create.html")


def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/users/new')

    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )
    return redirect('/users')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'update.html', context)

def update(request, user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/users/{}/edit'.format(user_id))

    updateuser = User.objects.get(id=user_id)
    updateuser.first_name = request.POST['first_name']
    updateuser.last_name = request.POST['last_name']
    updateuser.email = request.POST['email']
    updateuser.save()
    return redirect('/users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'show.html', context)


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')