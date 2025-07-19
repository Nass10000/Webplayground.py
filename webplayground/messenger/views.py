from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from .models import Thread, Message

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ThreadListView(TemplateView):
    template_name = 'messenger/thread_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['threads'] = Thread.objects.filter(users=self.request.user)
        return context

@method_decorator(login_required, name='dispatch')
class ThreadDetailView(TemplateView):
    template_name = 'messenger/thread_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        
        # Verificar que el usuario pertenece al hilo
        if self.request.user not in thread.users.all():
            raise Http404("No tienes acceso a esta conversación")
            
        context['thread'] = thread
        context['thread_messages'] = thread.messages.all()
        return context
    
    def post(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk)
        
        # Verificar que el usuario pertenece al hilo
        if request.user not in thread.users.all():
            raise Http404("No tienes acceso a esta conversación")
        
        content = request.POST.get('content', '').strip()
        if content:
            Message.objects.create(
                user=request.user,
                thread=thread,
                content=content
            )
            messages.success(request, "Mensaje enviado correctamente")
        else:
            messages.error(request, "El mensaje no puede estar vacío")
        
        return redirect('thread_detail', pk=pk)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    
    # No permitir conversaciones con uno mismo
    if user == request.user:
        messages.error(request, "No puedes enviar mensajes a ti mismo")
        return redirect('profile_detail', username=username)
    
    # Buscar o crear el hilo de conversación
    thread = Thread.objects.find_or_create(request.user, user)
    
    return redirect('thread_detail', pk=thread.pk)
