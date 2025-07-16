from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created', 'updated')
    search_fields = ('title', 'content')
    list_editable = ('order',)
    readonly_fields = ('created', 'updated')

admin.site.register(Page, PageAdmin)
