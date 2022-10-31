from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("STARTING PROJECT.....Main Page")

def about(request):
    return render(request,'first.html')

def contact(request):
    return HttpResponse("THIS IS MY CONTACT PAGE.......")

def detail(request):
    return render(request,'second.html')

def thanks(request):
    return HttpResponse("THANK YOU FOR YOUR VISIT..........")