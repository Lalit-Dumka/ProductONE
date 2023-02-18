from django.contrib import messages
# from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
	
def index(request):
	# context is dictionary using which we can send variables to an html file
	# render function displays the html file given to it as parameter
    # context = {
    #     "variable1":"test variable",
    # }
    # return render(request,'index.html', context)
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

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