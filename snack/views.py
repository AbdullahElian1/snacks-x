from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model= Snack

class SnackDetailView(DetailView):
    template_name= 'snack_detail.html'
    model= Snack
