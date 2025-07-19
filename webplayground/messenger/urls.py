from django.urls import path
from .views import ThreadListView, ThreadDetailView, start_thread

urlpatterns = [
    path('', ThreadListView.as_view(), name='messenger'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/start/<str:username>/', start_thread, name='start_thread'),
]
