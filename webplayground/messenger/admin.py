from django.contrib import admin
from .models import Thread, Message

# Register your models here.

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('created',)

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated')
    list_filter = ('updated',)
    filter_horizontal = ('users',)
    inlines = [MessageInline]
    
@admin.register(Message) 
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'thread', 'content', 'created')
    list_filter = ('created', 'user')
    search_fields = ('content', 'user__username')
    readonly_fields = ('created',)
