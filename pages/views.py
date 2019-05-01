from django.shortcuts import render
from posts.models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    posts = Post.objects.order_by('-post_time').filter(is_published=True)

    paginator = Paginator(posts, per_page=3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')


def comment_policy(request):
    return render(request, 'pages/comment-policy.html')