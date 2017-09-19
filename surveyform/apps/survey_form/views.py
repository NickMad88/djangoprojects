from django.shortcuts import render, HttpResponse, redirect

def index(request):


    return render(request, 'index.html')

def process(request):
    request.session['studentname'] =  request.POST['name']
    request.session['studentlocation'] = request.POST['location']
    request.session['studentcomment'] = request.POST['comment']
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] = request.session['counter'] + 1


    return redirect('/results')
# Create your views here.

def results(request):
    return render(request, 'results.html')