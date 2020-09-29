from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required

from .models import Post
from subreddits.models import Subreddit

from django.utils import timezone 
from posts.validate_post import ValidatePost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    posts = Post.objects.order_by('-pub_date')
    subreddits = Subreddit.objects.all()

    paginator = Paginator(subreddits, 5)
    page_number = request.GET.get('page')
    paged_subs = paginator.get_page(page_number)


    context = {
		'posts': posts,
        'subreddits': paged_subs
	}
    return render(request, 'posts/index.html', context)

def post(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)

    context = {
		'post': post,
	}
    return render(request, 'posts/post.html', context)

# @login_required(login_url='/accounts/signup')
def create(request):    
    validate_post = ValidatePost(request)

    if validate_post.is_create_post_valid():
        post = validate_post.create_post()
        return redirect('/posts/' + str(post.id))
    
    return render(request, 'posts/create.html', {'error': 'All fields are required to create a product.'})