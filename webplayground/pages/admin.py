from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created', 'updated')
    search_fields = ('title', 'content')
    list_editable = ('order',)
    readonly_fields = ('created', 'updated')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
