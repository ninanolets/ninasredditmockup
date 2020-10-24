from .models import Post
from subreddits.models import Subreddit
from django.utils import timezone

class ValidatePost():
    def __init__(self, request):
        self.request = request

    def create_post(self):
        subreddits = Subreddit.objects.all()
        post = Post() 
        
        post.pub_date = timezone.datetime.now()
        post.update_date = timezone.datetime.now()
        post.user = self.request.user

        post.title = self.request.POST['title'] 
        post.content = self.request.POST['content']

        try:
            post.photo = self.request.FILES['photo']
        except:
            post.photo = self.request.POST.get('photo', False)

        subreddit = self.request.POST['subreddit']
        post.subreddit = subreddits.get(slug=subreddit)

        post.save() 

        return post

    def is_create_post_valid(self):
        return (
            self.request.POST['subreddit'] and 
            self.request.POST['title'] and 
            (self.request.POST['content'] or
            self.request.FILES['photo'])
        )
    