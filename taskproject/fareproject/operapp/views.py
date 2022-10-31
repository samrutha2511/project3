from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def operation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return render(request,"result.html",{'add':a,'sub':b,'mul':c,'div':d })