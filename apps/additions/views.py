from django.shortcuts import render
from .models import Addition,Comment

# Create your views here.
def index(request):
    additions = Addition.objects.all()
    print(additions)
    context = {
        'additions' : additions
    }
    return render(request, 'additions/index.html', context)