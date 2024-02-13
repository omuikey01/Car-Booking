from django.shortcuts import render

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


def registerform(request):
    if request.method == "POST":
        pass
    return render(request, "base/index/auth.html", {"any_one" : "in"})
