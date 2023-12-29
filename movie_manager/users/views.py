from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,password=password)
        except Exception as e :
                error_message = str(e)
                userexists =  "duplicate key value violates unique constraint"
                if error_message.__contains__(userexists):
                     error_message = f'A User with this username: {username} already exists.'
    return render(request,'users/create.html',{'user':user,'error_message':error_message})

def login(request):
    error_message = None
    if request.POST:
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request,username=username,password=password)
         if user:
              authlogin(request,user)
              return redirect('home')
         else:
              error_message = 'invalid credentials'
        
    return render(request,'users/login.html',{'error_message':error_message})

@login_required(login_url='login')
def logout(request):
         authlogout(request)
         return redirect('login')

