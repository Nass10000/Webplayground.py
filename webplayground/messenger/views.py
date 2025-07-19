from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
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
    
    # Como User tiene relación con Thread via Many2Many, 
    # podemos acceder directamente en el template a request.user.threads.all
    # No necesitamos sobreescribir get_context_data

@method_decorator(login_required, name='dispatch')  
class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'messenger/thread_detail.html'
    context_object_name = 'thread'
    
    def get_object(self):
        # Obtener el hilo
        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        
        # Verificar que el usuario pertenece al hilo
        if self.request.user not in thread.users.all():
            raise Http404("No tienes acceso a esta conversación")
            
        return thread
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread_messages'] = self.object.messages.all()
        return context
    
    def post(self, request, pk):
        thread = self.get_object()
        
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
    
    # Buscar o crear el hilo de conversación usando nuestro Manager personalizado
    thread = Thread.objects.find_or_create(request.user, user)
    
    return redirect('thread_detail', pk=thread.pk)

@login_required
def add_message(request, pk):
    # Imprimir parámetros GET para debug
    print("Parámetros GET:", request.GET)
    
    # Crear la respuesta JSON inicialmente indicando que no se creó el mensaje
    json_response = {'created': False}
    
    if request.method == 'GET':
        # Obtener el hilo
        thread = get_object_or_404(Thread, pk=pk)
        
        # Verificar que el usuario pertenece al hilo
        if request.user not in thread.users.all():
            return JsonResponse({'created': False, 'error': 'No tienes acceso a esta conversación'})
        
        # Obtener el contenido del mensaje desde GET
        content = request.GET.get('content', '').strip()
        
        if content:
            # Crear el mensaje usando nuestro Manager que valida la seguridad
            message = Message.objects.create(
                user=request.user,
                thread=thread,
                content=content
            )
            
            if message:  # Si se creó correctamente (no es None)
                json_response['created'] = True
                json_response['message'] = {
                    'user': message.user.username,
                    'content': message.content,
                    'created': message.created.strftime('%d/%m/%Y %H:%M')
                }
    
    return JsonResponse(json_response)
