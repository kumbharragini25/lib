from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.shortcuts import render
from TeachersImages.models import ImageWithLabel
from toppers.models import TopperwithLabels
from farm.models import farm
from django.conf import settings
from IBT.models import News
from news.models import News1
from shetivpashupalan.models import News2
from urjavparyavaran.models import News3
from gruhvarogya.models import News4
from abhiyantriki.models import News5
from homepage.models import myhome
def topper_images(request):
    images=TopperwithLabels.objects.all()
    return render(request,"toppers.html",{'images':images})
def image_list(request):
    images = ImageWithLabel.objects.all()
    return render(request, 'imagesfromdatabase.html', {'images': images})
def display_first_three_images(request):
    # Retrieve the first three images from the database
    images = TopperwithLabels.objects.all()[:3]
    return render(request, 'index.html', {'images': images})   
    
# Create your views here.
def home(request):
    image=TopperwithLabels.objects.all()[:3]

    return render(request,"authentication/index.html",{'image':image})
def farmacy(request):
    info=farm.objects.all()
    return render(request,"farm.html",{'info':info})    
def ibt(request):
    info=News.objects.all()
    return render(request,"IBT.html",{'info':info})
def news(request):
    info=News1.objects.all()
    return render(request,"news.html",{'info':info})
def shetivpashupalan(request):
    info=News2.objects.all()
    return render(request,"shetivpashupalan.html",{'info':info})
def urjavparyavaran(request):
    info=News3.objects.all()
    return render(request,"urjavparyavaran.html",{'info':info})
def gruhvarogya(request):
    info=News4.objects.all()
    return render(request,"gruhvarogya.html",{'info':info})
def abhiyantriki(request):
    info=News5.objects.all()
    return render(request,"abhiyantriki.html",{'info':info})
def newsDetails(request,newsid):
    newsDetails=News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('psw')
        pass2=request.POST.get('psw-repeat')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        messages.success(request,"Your account is crated successfully")
        return redirect('signin')
    return render(request,"authentication/signup.html")
def signin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pass1=request.POST.get('psw')
        my_user=authenticate(username=uname,password=pass1)
        # name=my_user.first_name
        if my_user is not None:
            login(request,my_user)
            messages.success(request,"logged in successfully")
            return render(request,"index.html")
        else:
            return HttpResponse("Plese enter the valid username and password") 
    return render(request,"authentication/signin.html")
def signout(request):
    pass
def window(request):
    i=myhome.objects.all()
    return render(request,"index.html",{'info':i})
def about(request):
    return render(request,"about.html")