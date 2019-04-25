from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'post_time')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('author', 'title', 'body')
    list_per_page = 25


admin.site.register(Post, PostAdmin)
