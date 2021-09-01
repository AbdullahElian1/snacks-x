from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name = 'snacks/snack_list.html'
    model= Snack

class SnackDetailView(DetailView):
    template_name= 'snacks/snack_detail.html'
    model= Snack
class SnackCreateView(CreateView):
    template_name= 'snacks/snack_create.html'
    model= Snack
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name= 'snacks/snack_update.html'
    model= Snack
    fields = ['title', 'purchaser', 'description']
class SnackDeleteView(DeleteView):
    template_name= 'snacks/snack_delete.html'
    model= Snack
    success_url = reverse_lazy('snacks_list')