from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is home page")

def templates(request):
    return render(request, 'accounts/login.html')