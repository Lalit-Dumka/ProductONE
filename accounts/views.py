from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in !')
            return redirect("/")
        else:
            messages.warning(request, 'Invalid Credentials !')
            return render(request, 'registerUser.html')
    return render(request, 'registerUser.html')


@login_required
def logoutUser(request):
    logout(request)
    messages.warning(request, "Logged out successfully!")
    return redirect("/")

def register(request):
    if(request.method=='POST'):
        username = request.POST['logname']
        email = request.POST['logemail']
        password = request.POST['logpass']

        if(User.objects.filter(username=username).exists()):
            messages.error(request, "username already taken!")
            return render(request,'registerUser.html')
        elif(User.objects.filter(email=email).exists()):
            messages.error(request, "Account with this email already exists.. try logging in!")
            return render(request,'registerUser.html')
        else:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            print('User Created')
            messages.warning(request, "Created Account successfully!")
            return redirect('/')
    else:
        return render(request,'registerUser.html')