from typing import Any
from django.shortcuts import render,get_object_or_404, redirect
from .models import Addition,Comment, Favorite
from django.http import JsonResponse
from .forms import PostForm, CommentForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

class AdditionsListView(ListView):
    model = Addition
    template_name = 'additions/index.html'
    context_object_name = 'additions' 
    paginate_by = 3 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        if self.request.user.is_authenticated:
            context['favorite_additions'] = Favorite.objects.filter(user=self.request.user).values_list('addition_id', flat=True)
        return context


class PostCreateView(CreateView):
    model = Addition
    form_class = PostForm
    template_name = 'additions/additions.html'
    success_url = '/additions/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class AddFavoriteView(LoginRequiredMixin, View):
    def get(self, request, addition_id):
        user = request.user
        addition = get_object_or_404(Addition, id=addition_id)

        if not user.is_authenticated:
            return redirect('members:login')

        favorite = Favorite.objects.filter(user=user, addition=addition).first()
        
        if favorite:
            favorite.delete()
            status = 'removed'
        else:
            Favorite.objects.create(user=user, addition=addition)
            status = 'added'

        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(referer)
        
        

        
    
def get_detale(request, detale_id):
    detale = get_object_or_404(Addition,id=detale_id)
    form_comment = CommentForm()
    
    context = {
        'detale': detale,
        'comment_form': form_comment,
    }

    return render(request, 'additions/addition.html', context)



    
def comment(request, detale_id):
    detale = get_object_or_404(Addition, id=detale_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.detale = detale
            comment.author = request.user
            comment.save()
    return redirect('additions:detale', detale_id=detale_id)



def like_comment(request, detale_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()
    return JsonResponse({'likes': comment.likes})


        