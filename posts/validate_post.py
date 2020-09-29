from .models import Post
from subreddits.models import Subreddit

from django.utils import timezone

class ValidatePost():
    def __init__(self, request):
        self.request = request

    def create_post(self):
        post = Post() 
        
        post.title = self.request.POST['title'] 
        post.content = self.request.POST['content']
        post.photo = self.request.FILES['photo'] 
        post.pub_date = timezone.datetime.now()
        post.user = self.request.user
        
        post.subreddit = self.request.post

        # post.subreddit = self.request.id
        # post.subreddit = self.request.POST['subreddit']
        # post.subreddit = Subreddit.objects.filter(slug=self.request)


        post.save() 

        return post

    def is_create_post_valid(self):
        return (
            self.request.method == 'POST' and
            self.request.POST['title'] and 
            self.request.POST['content'] and
            self.request.FILES['photo']
        )
        