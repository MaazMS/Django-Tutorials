from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is home page")

def templates(request):
    return render(request, 'accounts/login.html')

def ginger(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Maaz'
    dictionary = {'myName' : name, 'numbers' : numbers}
    return  render(request, 'accounts/passing_value.html', dictionary )

def Home_extends_base(request):
    return render(request, 'accounts/home.html')