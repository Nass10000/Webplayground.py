from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'content')
    readonly_fields = ('created', 'updated')

admin.site.register(Page, PageAdmin)
