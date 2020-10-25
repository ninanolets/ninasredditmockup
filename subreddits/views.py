from django.shortcuts import render, get_object_or_404, redirect
from .models import Subreddit
from posts.models import Post
from postupvotes.models import Postupvote


from subreddits.validate_subreddit import ValidateSubreddit
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re


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

    context = {
		'posts': paged_posts,
        'subreddits': paged_subs,
        'upvotes': upvotes,
	}
    return render(request, 'subreddits/index.html', context)

def subreddit(request, slug):
    subreddit = get_object_or_404(Subreddit, slug=slug)
    posts = Post.objects.filter(subreddit_id=subreddit.id).annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
    upvotes = Postupvote.objects.filter(user_id=request.user.id)

    post_paginator = Paginator(posts, 10)
    post_page_number = request.GET.get('page')
    paged_posts = post_paginator.get_page(post_page_number)


    context = {
		'subreddit': subreddit,
        'posts': paged_posts,
        'upvotes': upvotes,
	}

    return render(request, 'subreddits/subreddit.html', context)

def all_subreddits(request):
    subreddits = Subreddit.objects.annotate(subreddit_posts=Count('sub_posts')).order_by('-subreddit_posts')

    context = {
		'subreddits': subreddits,
	}

    return render(request, 'subreddits/all_subreddits.html', context)


def create(request):
    if request.user.is_anonymous:
        messages.error(request, 'You must login to be able to create subreddits.')
    return create_2(request)

@login_required(login_url='/accounts/login')
def create_2(request):    
    subreddits = Subreddit.objects.all()
    validate_subreddit = ValidateSubreddit(request)

    if request.method == 'POST':
        if validate_subreddit.is_create_subreddit_valid():
            
            slug = re.sub('[^a-zA-Z0-9\.]', '_', request.POST['slug'])

            if subreddits.filter(slug=slug).exists():
                messages.error(request, 'Slug is already taken')
                return redirect('create_sub')
            else: 
                subreddit = validate_subreddit.create_subreddit()
                messages.success(request, 'You just created a subreddit!')
                return redirect('/s/' + str(slug))
        else:
            messages.error(request, 'All fields are required to create a subreddit') 
            return redirect('create_sub') 
    else: 
        return render(request, 'subreddits/create_sub.html')

@login_required(login_url='/accounts/login')
def delete_sub(request, subreddits_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddits_id)
    
    if request.user == subreddit.user:
        subreddit.delete() # or save edits
        messages.success(request, 'Successfully Deleted')
        return redirect('index')
    else:
        messages.error(request, 'Permission Denied')
        return redirect('/s/' + str(subreddit))

@login_required(login_url='/accounts/login')
def update_sub(request, slug):
    subreddit = get_object_or_404(Subreddit, slug=slug)    

    context = { 
        'subreddit': subreddit,
    }

    validate_subreddit = ValidateSubreddit(request)

    if request.method == 'POST':
        if request.POST['title'] and request.POST['content'] and request.FILES['photo']:

            subreddit.title = request.POST['title'] 
            subreddit.description = request.POST['content']   
            subreddit.photo = request.FILES['photo']     
            try:
                subreddit.avatar = request.FILES['avatar']
            except:
                subreddit.avatar = request.POST.get('avatar', False)
            
            subreddit.save()
            return redirect('/s/' + slug)
        return redirect('/s/' + slug)
    return render(request, 'subreddits/update_sub.html', context)
        

