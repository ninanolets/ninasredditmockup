from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Commupvote
from comments.models import Comment

@login_required(login_url='/accounts/login')
def upvote_comment(request, comments_id, posts_id):
    # if request.method == "POST": 
    comment = get_object_or_404(Comment, pk=comments_id)
    upvote = Commupvote.objects.filter(comment_id=comments_id, user_id=request.user.id)

    if upvote:
        upvote.delete()
        return redirect('/post/' + str(comment.post.id))
    else:
        upvote = Commupvote(comment_id=comments_id, user_id=request.user.id)
        upvote.save()
        return redirect('/post/' + str(comment.post.id))
    # else:
    #     return redirect('index')
