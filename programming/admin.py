from django.contrib import admin
from .models import Program, Python


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'date')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('author', 'title', 'body')
    list_per_page = 25

admin.site.register(Program, ProgramAdmin)


class PythonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'date')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('author', 'title', 'body')
    list_per_page = 25

admin.site.register(Python, PythonAdmin)
