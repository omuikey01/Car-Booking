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
    return render(request, "base/index/auth.html")