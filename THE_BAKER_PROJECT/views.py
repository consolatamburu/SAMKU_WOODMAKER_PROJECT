from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def edit(request):
    return render(request, 'edit.html')


def innerpage(request):
    return render(request, 'inner-page.html')


def portfolio(request):
    return render(request, 'portfolio-details.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username, password)
        myuser.save()
    return render(request, 'signup.html')

def handlelogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = authenticate(username=username,password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            return render(request, '/login')

    return render(request, 'signup.html')
