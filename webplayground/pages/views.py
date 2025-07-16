from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Page

# Create your views here.

class PageListView(ListView):
    model = Page
    # Django buscará automáticamente pages/page_list.html

class PageDetailView(DetailView):
    model = Page
    # Django buscará automáticamente pages/page_detail.html

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages')
