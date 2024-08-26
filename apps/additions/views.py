from django.shortcuts import render,get_object_or_404, redirect
from .models import Addition,Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    additions = Addition.objects.all()
    create_form = PostForm()
    context = {
        'additions' : additions,
        "form" : create_form,
    }
    return render(request, 'additions/index.html', context)


def get_detale(request, detale_id):
    detale = get_object_or_404(Addition,id=detale_id)
    
    context = {
        'detale': detale
    }
    
    return render(request, 'additions/addition.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('additions:index')