from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random

def index(request):
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'counter' not in request.session:
        request.session['counter'] = 0

    return render(request, "index.html")  

def process_money(request):
    
    if request.method == 'POST':

        if request.POST['building'] == 'farm_form':
            print "Hello!"
            goldroll = random.randint(10,20)
            request.session['counter'] = request.session['counter'] + goldroll
            content = {
                'text': "Earned {} from the farm!".format(goldroll),
                'color': 'green'
            }
            request.session['activities'].append(content)

        elif request.POST['building'] == "cave_form":
            goldroll = random.randint(5,10)
            request.session['counter'] = request.session['counter'] + goldroll
            content = {
                'text': "Earned {} from the cave!".format(goldroll),
                'color': 'green'
            }
            request.session['activities'].append(content)

        elif request.POST['building'] == "house_form":
            goldroll = random.randint(2,5)
            request.session['counter'] = request.session['counter'] + goldroll
            content = {
                'text': "Earned {} from the house!".format(goldroll),
                'color': 'green'
            }
            request.session['activities'].append(content)

        elif request.POST['building'] == "casino_form":
            goldroll = random.randint(-50,50)
            if goldroll < 0:
                request.session['counter'] = request.session['counter'] + goldroll
                content = {
                'text': "Entered a casino and lost {} gold...OUCH!".format(-1*goldroll),
                'color': 'red'
                }
                request.session['activities'].append(content)

            elif goldroll >= 0:
                request.session['counter'] = request.session['counter'] + goldroll
                content = {
                'text': "Entered a casino and won {} gold...NICE!".format(goldroll),
                'color': 'green'
                }
                request.session['activities'].append(content)

    return redirect('/')

def reset(request):
    request.session['activities'] = []
    request.session['counter'] = 0

    return redirect('/')