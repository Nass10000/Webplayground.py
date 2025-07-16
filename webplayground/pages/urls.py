from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='page'),
]
