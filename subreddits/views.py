from django.shortcuts import render, get_object_or_404
from .models import Subreddit

def index(request):
    return render(request, 'subreddits/subreddits.html')

def subreddit(request, subreddits_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddits_id)
    
    context = {
		'subreddit': subreddit
	}

    return render(request, 'subreddits/subreddit.html', context)
