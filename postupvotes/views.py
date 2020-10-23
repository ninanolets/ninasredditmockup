from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Postupvote
from posts.models import Post
from django.contrib import messages

def upvote_post(request, posts_id):
    if request.user.is_anonymous:
        messages.error(request, 'You must be logged in to upvote posts.')
    return upvote_post_2(request, posts_id)

@login_required(login_url='/accounts/login')
def upvote_post_2(request, posts_id):
    post = get_object_or_404(Post, id=posts_id) 

    upvote = Postupvote.objects.filter(post_id=posts_id, user_id=request.user.id)

    if upvote:
        upvote.delete()
        return redirect('/s/' + str(post.subreddit) + '/post/' + str(posts_id))
    else:
        upvote = Postupvote(post_id=posts_id, user_id=request.user.id)
        upvote.save()
        return redirect('/s/' + str(post.subreddit) + '/post/' + str(posts_id))
    # else:
    #     return redirect('index')


