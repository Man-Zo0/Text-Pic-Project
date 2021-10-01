from django.shortcuts import redirect, render, get_object_or_404
from .models import Images

# Create your views here.

def home(request, id):
    info = get_object_or_404(Images, pk = id) 
    return render(request, 'home.html',{'info': info})

def start(request):
    return redirect('home', 1)