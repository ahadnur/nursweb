from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problem
from .forms import ProblemForm


def index(request):

    problems = Problem.objects.order_by('-time')
    paginator = Paginator(problems, 5)
    page = request.GET.get('page')
    paged_problems = paginator.get_page(page)

    context = {
        'problems': paged_problems
    }

    return render(request, 'problem/problems.html', context)


def problem(request, slug_text):
    problem = get_object_or_404(Problem, slug=slug_text)
    context = {
        'problem': problem
    }
    return render(request, 'problem/problem.html', context)


def add_problem(request):
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('problems')
    else:
        form = ProblemForm()
    return render(request, 'problem/add_problem.html', {'form': form})
