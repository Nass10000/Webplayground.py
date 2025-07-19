from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(
            Q(users=user1) & Q(users=user2)
        ).distinct()
        if queryset.count() == 1:
            return queryset.first()
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    updated = models.DateTimeField(auto_now=True)
    
    objects = ThreadManager()
    
    class Meta:
        ordering = ['-updated']
        
    def __str__(self):
        if self.users.count() == 2:
            users = list(self.users.all())
            return f"Conversación entre {users[0].username} y {users[1].username}"
        return f"Conversación {self.pk}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return f"Mensaje de {self.user.username} en {self.thread}"
