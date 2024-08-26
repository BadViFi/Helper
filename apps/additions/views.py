from django.shortcuts import render,get_object_or_404, redirect
from .models import Addition,Comment

# Create your views here.
def index(request):
    additions = Addition.objects.all()
    context = {
        'additions' : additions
    }
    return render(request, 'additions/index.html', context)


def get_detale(request, detale_id):
    detale = get_object_or_404(Addition,id=detale_id)
    
    context = {
        'detale': detale
    }
    
    return render(request, 'additions/addition.html', context)
