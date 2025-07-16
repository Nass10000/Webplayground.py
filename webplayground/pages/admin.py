from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'
    
admin.site.register(Page, PageAdmin)
