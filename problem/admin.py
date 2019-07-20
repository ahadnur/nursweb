from django.contrib import admin
from .models import Problem


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'problem_setter', 'time')
    list_display_links = ('id', 'title')
    list_filter = ('problem_setter',)
    search_fields = ('problem_setter', 'title', 'body')
    list_per_page = 25


admin.site.register(Problem, ProblemAdmin)
