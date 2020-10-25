from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Post
from subreddits.models import Subreddit
from comments.models import Comment
from postupvotes.models import Postupvote
from commupvotes.models import Commupvote

from django.utils import timezone 
from posts.validate_post import ValidatePost

from django.contrib import messages
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

def post(request, posts_id, slug):
    post = get_object_or_404(Post, pk=posts_id)
    subreddit = get_object_or_404(Subreddit, slug=slug)
    comments = Comment.objects.filter(post_id=posts_id).order_by('-pub_date')
    has_user_voted = Postupvote.objects.filter(post_id=posts_id, user_id=request.user.id).exists()
    has_user_voted_comm = Commupvote.objects.filter(user_id=request.user.id)
    
    context = {
		'post': post,
        'subreddit': subreddit,
        'comments': comments,
        'has_user_voted': has_user_voted,
        'has_user_voted_comm': has_user_voted_comm,
	}

    return render(request, 'posts/post.html', context)

def create(request, slug):
    if request.user.is_anonymous:
        messages.error(request, 'You must login to be able to create posts.')
    return create_2(request, slug)

@login_required(login_url='/accounts/login')
def create_2(request, slug):
    subreddit = get_object_or_404(Subreddit, slug=slug)    
    validate_post = ValidatePost(request)

    context = { 
        'subreddit': subreddit
    }

    if request.method == 'POST':
        if validate_post.is_create_post_valid():

            s_slug = request.POST['subreddit']
            
            if not Subreddit.objects.filter(slug=s_slug).exists():
                messages.error(request, 'Subreddit does not exits')
                return redirect('create_from_index')
                
            else:
                post = validate_post.create_post()
                return redirect('/s/' + slug + '/post/' + str(post.id))



            post = validate_post.create_post()
            return redirect('/s/' + slug + '/post/' + str(post.id))
        else: 
            messages.error(request, 'All fields are required to create a post')
            return redirect('create')
    else: 
        return render(request, 'posts/create.html', context)

def create_from_index(request):
    if request.user.is_anonymous:
        messages.error(request, 'You must login to be able to create posts.')
    return create_from_index_2(request)

@login_required(login_url='/accounts/login')
def create_from_index_2(request):   
    validate_post = ValidatePost(request)

    if request.method == 'POST':
        if validate_post.is_create_post_valid():
            slug = request.POST['subreddit']
            
            if Subreddit.objects.filter(slug=slug).exists():
                post = validate_post.create_post()
                return redirect('/s/' + slug + '/post/' + str(post.id))
            else:
                messages.error(request, 'Subreddit does not exits')
                return redirect('create_from_index')
        else: 
            messages.error(request, 'All fields are required to create a post')
            return redirect('create_from_index')
    else: 
        return render(request, 'posts/create_from_index.html')


@login_required(login_url='/accounts/login')
def delete_post(request, posts_id):
    post = get_object_or_404(Post, pk=posts_id)

    post.delete() # or save edits
    messages.success(request, 'Successfully Deleted')
    return redirect('index')

@login_required(login_url='/accounts/login')
def update_post(request, slug, posts_id):
    post = get_object_or_404(Post, pk=posts_id)
    subreddit = get_object_or_404(Subreddit, slug=slug)    

    context = { 
        'subreddit': subreddit,
        'post': post,
    }

    validate_post = ValidatePost(request)

    if request.method == 'POST':
        if request.POST['title'] and (request.POST['content'] or request.FILES['photo']):

            post.title = request.POST['title']
            post.content = request.POST['content']
            try:
                post.photo = request.FILES['photo']
            except:
                post.photo = request.POST.get('photo', False)

            post.update_date = timezone.datetime.now()

            post.save()
            return redirect('/s/' + slug + '/post/' + str(posts_id))
        return redirect('/s/' + slug + '/post/' + str(posts_id))
    return render(request, 'posts/update_post.html', context)
        

