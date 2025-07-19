from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/start/<username>/', views.start_thread, name='start_thread'),
    path('thread/<int:pk>/add_message/', views.add_message, name='add_message'),
]
