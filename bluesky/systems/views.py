from django.shortcuts import render
from django.http import HttpResponse
from requests import request


# Create your views here.
def home(request):
    return render(request, 'systems/dashboard.html')

def about_us(request):
    return render(request, 'systems/about_us.html')

def our_solutions(request):
    return render (request, 'systems/our_solutions.html')

def our_products(request):
    return render (request, 'systems/our_products.html')

def our_clients(request):
    return render (request, 'systems/our_clients.html')
    
def blogs(request):
    return render (request, 'systems/blogs.html')
