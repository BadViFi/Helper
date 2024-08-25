from django.shortcuts import render
from .models import Addition,Comment

# Create your views here.
def index(request):
    additions = Addition.objects.all()
    context = {
        'additions' : additions
    }
    return render(request, 'additions/index.html', context)


def get_detale(request,addition_id):
    detale = Addition.objects.get(id=addition_id)
    
    context = {
        'detale' : detale
    }
    
    return render(request, 'additions/additions.html', context)