from django.shortcuts import render, get_object_or_404
from .models import Program, Python
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):

    programs = Program.objects.order_by('-date').filter(is_published=True)
    paginator = Paginator(programs, 3)
    page = request.GET.get('page')
    paged_programs = paginator.get_page(page)

    context = {
        'programs': paged_programs
    }
    return render(request, 'program/programs.html', context)


def programming_post(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    context = {
        'program': program
    }
    return render(request, 'program/program_post.html', context)


def python(request):
    pythons = Python.objects.order_by('-date').filter(is_published=True)
    paginator = Paginator(pythons, 3)
    page = request.GET.get('page')
    paged_programs = paginator.get_page(page)

    context = {
        'pythons': paged_programs
    }
    return render(request, 'python/python_posts.html', context)


def python_post(request, slug_text):
    post = get_object_or_404(Python, slug=slug_text)
    context = {
        'post': post
    }
    return render(request, 'python/python_post.html', context)