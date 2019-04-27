from django.shortcuts import render, get_object_or_404
from posts.models import Post
from programming.models import Program
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    posts = Post.objects.order_by('-post_time').filter(is_published=True)
    
    paginator = Paginator(posts, per_page=3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts,
    }
    return render(request, 'posts/posts.html', context)


def post(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)