from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Marker
from .serializers import MarkerSerializer
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import MarkerForm
from django.contrib.auth.mixins import LoginRequiredMixin




class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class MapView(TemplateView):
    template_name = 'map/map.html'
    
    
class MarkerDescriptionView(DetailView):
    model = Marker
    template_name = 'map/description.html'
    context_object_name = 'marker'
    pk_url_kwarg = 'id'
    


@login_required
def add_marker(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            marker = form.save(commit=False)
            marker.user = request.user
            marker.save()
            return redirect('map:map_view')
    else:
        form = MarkerForm()
    return render(request, 'map/marker_form.html', {'form': form})