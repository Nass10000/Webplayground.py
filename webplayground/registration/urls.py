from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdateView, EmailUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile_email'),
]
