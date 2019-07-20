from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problem


def index(request):

    problems = Problem.objects.order_by('-time')
    paginator = Paginator(problems, 5)
    page = request.GET.get('page')
    paged_problems = paginator.get_page(page)

    context = {
        'problems': paged_problems
    }

    return render(request, 'problem/problems.html', context)


def problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {
        'problem': problem
    }
    return render(request, 'problem/problem.html', context)
