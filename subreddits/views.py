from django.shortcuts import render

def index(request):
    return render(request, 'subreddits/subreddits.html')

# def subreddit(request):
#     subreddit = get_object_or_404(Subreddit, pk=subreddits_id)
#     context = {
# 		'subreddit': subreddit
# 	}

#     return render(request, 'subreddits/subreddit.html', context)