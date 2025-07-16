from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
