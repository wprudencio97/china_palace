from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'menu/home.html')

def menu(request):
    return render(request, 'menu/menu.html')