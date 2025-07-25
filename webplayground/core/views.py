from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi súper Web Playground'
        return context

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
