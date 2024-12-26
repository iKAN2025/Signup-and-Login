from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users_list')

def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('users_list')
    return render(request,'edit_user.html',{'user':user})

def users_list(request):
    users = User.objects.all()
    return render(request, 'user_table.html', {'users': users})

def signupview(request):
    if request.method=='POST':

        myuser=User.objects.create_user(username = request.POST['username'],email = request.POST['email'],first_name = request.POST['first_name'],last_name = request.POST['last_name'],password = request.POST['password'])
        myuser.save()
        messages.success(request, 'Form submission successful')
        return redirect('login')

    return render(request,'signup.html')

def dashboard(request):
    # This is where you would gather any user data you need
    return render(request, 'dashboard.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,'dashboard.html')
        else:
            return redirect('signup')
    return render(request,'login.html')



