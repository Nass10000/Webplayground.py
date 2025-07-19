from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from registration.models import Profile

# Create your views here.

class ProfileListView(ListView):
    model = User
    template_name = 'profiles/profile_list.html'
    context_object_name = 'users'
    paginate_by = 3  # Mostrar 3 perfiles por página
    
    def get_queryset(self):
        # Solo mostrar usuarios que tienen un perfil
        return User.objects.filter(profile__isnull=False).select_related('profile')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
