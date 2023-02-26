from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()


from accounts.models import Customer, Seller
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('logUsername')
        # email = request.POST.get('logemail')
        password = request.POST.get('loginpassword')
        user = authenticate( username=username, password = password)
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
        username = request.POST['registerUsername']
        name = request.POST['registerName'].split(' ', 1)
        email = request.POST['registerEmail']
        password = request.POST['registerPassword']

        if(User.objects.filter(username=username).exists()):
            messages.error(request, "username already taken!")
            return render(request,'registerUser.html')
        if(User.objects.filter(email=email).exists()):
            messages.error(request, "Account with this email already exists.. try logging in!")
            return render(request,'registerUser.html')
        else:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            user.first_name = name[0]
            user.last_name = name[1]
            user.save()
            customer_c = Customer.objects.create(user=user,roomsStayed=0)
            customer_c.save()
            print('User Created')
            messages.warning(request, "Created Account successfully!")
            return redirect('/')
    else:
        return render(request,'registerUser.html')
def registerSeller(request):
    if(request.method=='POST'):
        username = request.POST['registerUsername']
        name = request.POST['registerName'].split(' ', 1)
        phone= request.POST['registerPhone']
        email = request.POST['registerEmail']
        password = request.POST['registerPassword']

        if(User.objects.filter(username=username).exists()):
            messages.error(request, "username already taken!")
            return render(request,'registerUser.html')
        elif(User.objects.filter(email=email).exists()):
            messages.error(request, "Account with this email already exists.. try logging in!")
            return render(request,'registerUser.html')
        elif(User.objects.filter(phone_number=phone).exists()):
            messages.error(request, "You have already registered.. try logging in!")
            return render(request,'registerUser.html')
        else:
            c=User.objects.create_user( email=email, username = username, password=password)
            c.save()
            c.phone_number = phone
            c.is_seller = True
            c.first_name = name[0]
            c.last_name = name[1]
            c.save()
            customer_c = Customer.objects.create(user=c,roomsStayed=0)
            seller_c = Seller.objects.create(user=c,roomCount=0, rating =0)
            customer_c.save()
            seller_c.save()
            print('User Created')
            messages.warning(request, "Created Account successfully!")
            return redirect('/')
    else:
        return render(request,'registerUser.html')