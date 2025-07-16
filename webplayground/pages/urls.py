from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreateView.as_view(), name='pages_create'),
]
