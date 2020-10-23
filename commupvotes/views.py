from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Commupvote
from comments.models import Comment
from django.contrib import messages


def upvote_comment(request, slug, comments_id, posts_id):
    if request.user.is_anonymous:
        messages.error(request, 'You must login to upvote comments.')
    return upvote_comment_2(request, slug, comments_id, posts_id)

@login_required(login_url='/accounts/login')
def upvote_comment_2(request, slug, comments_id, posts_id):
    # if request.method == "POST": 
    comment = get_object_or_404(Comment, pk=comments_id)
    upvote = Commupvote.objects.filter(comment_id=comments_id, user_id=request.user.id)

    

    if upvote:
        upvote.delete()
        # return redirect('/post/' + str(comment.post.id))
        return redirect('/s/' + slug + '/post/' + str(posts_id))
    else:
        upvote = Commupvote(comment_id=comments_id, user_id=request.user.id)
        upvote.save()
        return redirect('/s/' + slug + '/post/' + str(posts_id))
    # else:
    #     return redirect('index')
