from django.shortcuts import render, get_object_or_404, redirect
from .models import Subreddit
from posts.models import Post

from subreddits.validate_subreddit import ValidateSubreddit
from django.contrib.auth.decorators import login_required


def subreddit(request, subreddits_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddits_id)
    posts = Post.objects.filter(subreddit_id=subreddits_id).order_by('-pub_date')

    context = {
		'subreddit': subreddit,
        'posts': posts,
	}

    return render(request, 'subreddits/subreddit.html', context)

@login_required(login_url='/accounts/login')
def create(request):    
    validate_subreddit = ValidateSubreddit(request)

    if request.method == 'POST':
        if validate_subreddit.is_create_subreddit_valid():
            subreddit = validate_subreddit.create_subreddit()
            return redirect('/subreddits/' + str(subreddit.id))
    
        else: 
            return render(request, 'subreddits/create_sub.html', {'error': 'All fields are required to create a product.'})
    else: 
        return render(request, 'subreddits/create_sub.html')
    

    