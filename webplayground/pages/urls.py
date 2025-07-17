from django.urls import path
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm
from . import views

urlpatterns = [
    path('', ListView.as_view(model=Page), name='pages'),
    path('<int:pk>/', DetailView.as_view(model=Page), name='page'),
    path('create/', staff_member_required(
        CreateView.as_view(
            model=Page,
            form_class=PageForm,
            success_url='/pages/'
        )
    ), name='pages_create'),
    path('update/<int:pk>/', views.PageUpdateView.as_view(), name='pages_update'),
    path('delete/<int:pk>/', staff_member_required(
        DeleteView.as_view(
            model=Page,
            success_url='/pages/'
        )
    ), name='pages_delete'),
]
