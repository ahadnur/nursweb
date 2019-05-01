from django.shortcuts import render
from posts.models import Post

def index(request):
    posts = Post.objects.order_by('-post_time').filter(is_published=True)[:3]
    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')


def comment_policy(request):
    return render(request, 'pages/comment-policy.html')