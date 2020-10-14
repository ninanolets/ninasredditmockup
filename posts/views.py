from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Post
from subreddits.models import Subreddit
from comments.models import Comment
from postupvotes.models import Postupvote
from commupvotes.models import Commupvote


from django.utils import timezone 
from posts.validate_post import ValidatePost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.core.exceptions import PermissionDenied


def index(request):
    posts = Post.objects.annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
    subreddits = Subreddit.objects.annotate(subreddit_posts=Count('sub_posts')).order_by('-subreddit_posts')
    upvotes = Postupvote.objects.filter(user_id=request.user.id)


    sub_paginator = Paginator(subreddits, 3)
    sub_page_number = request.GET.get('page')
    paged_subs = sub_paginator.get_page(sub_page_number)

    post_paginator = Paginator(posts, 15)
    post_page_number = request.GET.get('page')
    paged_posts = post_paginator.get_page(post_page_number)

    # MAKE POST PAGINATION

    context = {
		'posts': paged_posts,
        'subreddits': paged_subs,
        'upvotes': upvotes,
	}
    return render(request, 'posts/index.html', context)

def post(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)
    comments = Comment.objects.filter(post_id=posts_id).order_by('-pub_date')
    has_user_voted = Postupvote.objects.filter(post_id=posts_id, user_id=request.user.id).exists()
    has_user_voted_comm = Commupvote.objects.filter(user_id=request.user.id)

    context = {
		'post': post,
        'comments': comments,
        'has_user_voted': has_user_voted,
        'has_user_voted_comm': has_user_voted_comm,
	}

    return render(request, 'posts/post.html', context)

def create(request):
    if request.user.is_anonymous:
        messages.error(request, 'You must login to be able to create posts.')
    return create_2(request)

@login_required(login_url='/accounts/login')
def create_2(request):    
    subreddits = Subreddit.objects.all()
    validate_post = ValidatePost(request)
    context = { 
        'subreddits': subreddits 
    }

    if request.method == 'POST':
        if validate_post.is_create_post_valid():
            post = validate_post.create_post()
            return redirect('/post/' + str(post.id))
        else: 
            messages.error(request, 'All fields are required to create a post')
            return redirect('create')
    else: 
        return render(request, 'posts/create.html', context)

@login_required(login_url='/accounts/login')
def delete_post(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)
    
    # if request.user == post.user:
    post.delete() # or save edits
    messages.success(request, 'Successfully Deleted')
    return redirect('index')
    # else:
    #     messages.error(request, 'Permission Denied')
    #     return redirect('/post/' + str(post.id))

    

