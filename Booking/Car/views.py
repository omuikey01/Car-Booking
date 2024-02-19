from django.shortcuts import render
import datetime
from datetime import time
from .models import *

# Create your views here.

def homepage(request):
    return render(request, "base/index/index.html")

def about(request):
    return render(request, "base/index/about/about.html")

def allshow(request):
    return render (request, "base/pages/all_data.html")

def drop_search(request):
    return render (request, "base/index/drop/drop_search.html")


def map_single_detail(request) :
    return render(request, "base/index/map/map_single_detail.html")

def product_details(request):
    return render(request, "base/pages/details.html")

def book_now(request):
    return render(request, "base/pages/payment.html")

def payment_done(request):
    return render(request, "base/pages/message.html")


def auth(request):
    if request.method == 'POST':
        any_one = request.POST['autu_btn']
        return render(request, "base/index/auth.html", {"any_one" : any_one})
    else :
        return render(request, "base/index/auth.html")
    

def auth_form_up(request):
    return render(request, "base/index/auth.html", {"any_one" : "up"})

def auth_form_in(request):
    return render(request, "base/index/auth.html", {"any_one" : "in"})

def forgotpass(request):
    return render(request, "base/auth/forgetpass.html")   

def registerform(request):
    if request.method == "POST":
        name = request.POST['signup-user_name']
        email = request.POST['signup-user_email']
        contact = request.POST['signup-user_contact']
        auto = request.POST['checkbox']
        password = request.POST['signup-user_pass']
        confirm = request.POST['signup-user_confirmpass']
        date = datetime.datetime.now()
        current_time = date.strftime("%Y-%m-%d, %H:%M:%S")

        if password != confirm:
            return render(request, "base/index/auth.html", {"any_one" : "up", "error" : "Password and Confirm password not match "})
        if auto == "Client":
            try:
                user = RegisterUser.objects.filter(user_email = email)
                if user:
                    return render(request, "base/index/auth.html", {"any_one" : "up", "error" : "Email already exists "})
                else :
                    RegisterUser.objects.create(user_name = name,user_email = email, user_contact = contact,user_auth =  auto, user_pass = password,user_join = current_time )
            except :
                RegisterUser.objects.create(user_name = name,user_email = email, user_contact = contact,user_auth =  auto, user_pass = password,user_join = current_time )     
        else :
            try :
                user = RegisterUser.objects.filter(dealer_email = email)
                if user:
                    return render(request, "base/index/auth.html", {"any_one" : "up", "error" : "Email already exists "})
                else :
                    RegisterDealer.objects.create(dealer_name = name,dealer_email = email,dealer_contact = contact, dealer_auth =  auto, dealer_pass = password, dealer_join = current_time )
            except :
                RegisterDealer.objects.create(dealer_name = name,dealer_email = email, dealer_contact = contact,dealer_auth = auto, dealer_pass = password, dealer_join = current_time)
        return render(request, "base/index/auth.html", {"any_one" : "in", "error" : "Now Login"})
    else :
        return render(request, "base/index/auth.html", {"any_one" : "in"})

def loginform(request):
    if request.method == 'POST':
        email = request.POST['signin-user_email']
        password = request.POST['signin-user_pass']
        auto = request.POST['checkbox']
        if auto == "Client" :
            try:
                user = RegisterUser.objects.get(user_email = email)
                if user.user_email == email and user.user_pass == password :
                    request.session['user_id'] = user.id
                    return render(request, "client/desh.html")
                else :
                  
                    return render(request, "base/index/auth.html", {"any_one" : "in","error" : " Invalid username or password "})
            except :
                    return render(request, "base/index/auth.html", {"any_one" : "up","error" : "User have't register please, do it"})  
        else :
            try:
                dealer = RegisterDealer.objects.get(dealer_email = email)
                if dealer.dealer_email == email and dealer.dealer_pass == password :
                    request.session['dealer_id'] = dealer.id
                    return render(request, "dealer/desh.html")
                else :
                    return render(request, "base/index/auth.html", {"any_one" : "in","error" : "Invalid username or password"})
            except :
                    return render(request, "base/index/auth.html", {"any_one" : "up","error" : "User have't register please, do it"})
    else :
        try :
           id = request.session.get("dealer_id")
           return render(request, "dealer/desh.html")
        except :
            id = request.session.get("user_id")
            return render(request, "client/desh.html")
        else :
            return render(request, "base/index/auth.html", {"any_one" : "in"})