from django.shortcuts import render,get_object_or_404, redirect
from .models import Addition,Comment
from django.http import JsonResponse
from .forms import PostForm, CommentForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# Create your views here.

class AdditionsListView(ListView):
    model = Addition
    template_name = 'additions/index.html'
    context_object_name = 'additions' 
    paginate_by = 3 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context



class PostCreateView(CreateView):
    model = Addition
    form_class = PostForm
    template_name = 'additions/additions.html'
    success_url = '/additions/'

    def form_valid(self, form):
        return super().form_valid(form)







# def index(request):
#     additions = Addition.objects.all()
#     create_form = PostForm()
#     context = {
#         'additions' : additions,
#         "form" : create_form,
#     }
#     return render(request, 'additions/index.html', context)


def get_detale(request, detale_id):
    detale = get_object_or_404(Addition,id=detale_id)
    form_comment = CommentForm()
    
    context = {
        'detale': detale,
        'comment_form': form_comment,
    }
    
    return render(request, 'additions/addition.html', context)


# def create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     return redirect('additions:index')

def comment(request, detale_id):
    detale = get_object_or_404(Addition, id=detale_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.detale = detale
            comment.save()
    return redirect('additions:detale', detale_id=detale_id)



def like_comment(request, detale_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()
    return JsonResponse({'likes': comment.likes})
