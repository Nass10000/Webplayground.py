from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm

# Create your views here.

# Las siguientes vistas se han movido a urls.py para simplificar el código:
# - PageListView -> ListView.as_view(model=Page)
# - PageDetailView -> DetailView.as_view(model=Page)
# - PageCreateView -> CreateView con decorador en urls.py
# - PageDeleteView -> DeleteView con decorador en urls.py

# Solo mantenemos PageUpdateView porque tiene un método personalizado get_success_url
@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages_update', args=[self.object.id]) + '?ok'
