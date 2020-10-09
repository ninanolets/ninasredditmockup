from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Postupvote

@login_required(login_url='/accounts/login')
def upvote_post(request, posts_id):
    # if request.method == "POST": 
    upvote = Postupvote.objects.filter(post_id=posts_id, user_id=request.user.id)
    # post_to_upvote = Post.objects.get(id=posts_id)

    if upvote:
        upvote.delete()
        return redirect('/post/' + str(posts_id))
    else:
        upvote = Postupvote(post_id=posts_id, user_id=request.user.id)
        upvote.save()
        return redirect('/post/' + str(posts_id))
    # else:
    #     return redirect('index')
