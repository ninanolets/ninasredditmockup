from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


from posts.models import Post
from .models import Comment

@login_required(login_url='/accounts/login')
def create_comment(request, posts_id, slug):
    if request.method == 'POST':
        if request.POST['comment_content']:
            comment = Comment()

            comment.pub_date = timezone.datetime.now()
            comment.user = request.user
            comment.post = Post.objects.get(id=posts_id)

            comment.content = request.POST['comment_content']

            comment.save()

            messages.success(request, 'Your comment was published')
            # return redirect('/post/' + str(comment.post.id))
            return redirect('/s/' + slug + '/post/' + str(comment.post.id))
        else:
            messages.error(request, 'Your comment is invalid')
            return redirect('/s/' + slug + '/post/' + str(comment.post.id))
    else:
        return redirect('/s/' + slug + '/post/' + str(comment.post.id))

@login_required(login_url='/accounts/login')
def delete_comment(request, slug, comment_post, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.post = Post.objects.get(id=comment_post)
    
    # if request.user == comment.user:
    comment.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('/s/' + slug + '/post/' + str(comment.post.id))
    # else:
    #     messages.error(request, 'Permission Denied')
    #     return redirect('/post/' + str(comment.post.id))
