from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'signin.html')

def register(request):
    return render(request,'signup.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')
