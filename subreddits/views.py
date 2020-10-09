from django.shortcuts import render, get_object_or_404, redirect
from .models import Subreddit
from posts.models import Post

from subreddits.validate_subreddit import ValidateSubreddit
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.exceptions import PermissionDenied


def subreddit(request, subreddits_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddits_id)
    posts = Post.objects.filter(subreddit_id=subreddits_id).order_by('-pub_date')

    context = {
		'subreddit': subreddit,
        'posts': posts,
	}

    return render(request, 'subreddits/subreddit.html', context)

def all_subreddits(request):
    subreddits = Subreddit.objects.order_by('-pub_date')

    context = {
		'subreddits': subreddits,
	}

    return render(request, 'subreddits/all_subreddits.html', context)

@login_required(login_url='/accounts/login')
def create(request):    
    validate_subreddit = ValidateSubreddit(request)

    if request.method == 'POST':
        if validate_subreddit.is_create_subreddit_valid():
            subreddit = validate_subreddit.create_subreddit()
            messages.success(request, 'You just created a subreddit!')
            return redirect('/subreddit/' + str(subreddit.id))
        else:
            messages.error(request, 'All fields are required to create a subreddit') 
            return redirect(request, 'create_sub') 
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
        return redirect('/subreddit/' + str(subreddit.id))
