from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print "*"*50  # more on session below
        return redirect("/")
    else:
        return render(request, "blogs_app/index.html/")

def show(request, number):
    return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
    return HttpResponse("placeholder to edit blog " + number)

def destroy(request, number):
    return redirect('/blogs')