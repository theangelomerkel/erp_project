from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Kunde

class KundeListView(ListView):
    model = Kunde
    template_name = 'kunde_list.html'

class KundeDetailView(DetailView):
    model = Kunde
    template_name = 'kunde_detail.html'

class KundeCreateView(CreateView):
    model = Kunde
    template_name = 'kunde_form.html'
    fields = '__all__'

class KundeUpdateView(UpdateView):
    model = Kunde
    template_name = 'kunde_form.html'
    fields = '__all__'

class KundeDeleteView(DeleteView):
    model = Kunde
    template_name = 'kunde_confirm_delete.html'
    success_url = reverse_lazy('kunde_list') 