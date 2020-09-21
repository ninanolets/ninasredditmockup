from django.shortcuts import render, get_object_or_404
from .models import Post
from subreddits.models import Subreddit

def index(request):
    posts = Post.objects.order_by('-pub_date')
    subreddits = Subreddit.objects.all()
    
    context = {
		'posts': posts,
        'subreddits': subreddits
	}
    return render(request, 'posts/index.html', context)

def post(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)
    subreddit = Subreddit.objects.all()

    context = {
		'post': post,
        'subreddit': subreddit
	}
    return render(request, 'posts/post.html', context)
