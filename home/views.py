from django.contrib import messages
from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse,redirect
	
def index(request):
	# context is dictionary using which we can send variables to an html file
	# render function displays the html file given to it as parameter
    # context = {
    #     "variable1":"test variable",
    # }
    # return render(request,'index.html', context)
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

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
            return render(request, 'login.html')
    return render(request, 'login.html')


@login_required
def logoutUser(request):
    logout(request)
    messages.warning(request, "Logged out successfully!")
    return redirect("homepage")

def signupUser(request):
    return render(request,'signup.html')
def listProperty(request):
    # return render(request,'listProperty.html')
    return HttpResponse("this is list  property page")
def reviews(request):
    # return render(request,'reviews.html')
    return HttpResponse("this is Reviews page")
def contact(request):
	#we can handle forms like this but for in order to save the data we need to create a MODEL(database)
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     contact = Contact(name=name, email=email, phone = phone, desc=desc, date=datetime.today())
    #     contact.save()
    #     messages.success(request, 'your message is sent!')
    # return render(request,'contact.html')
    return HttpResponse("this is contact us page")
def cityRooms(request):
    return render(request,'cityRooms.html')