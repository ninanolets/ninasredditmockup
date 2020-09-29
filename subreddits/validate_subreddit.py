from .models import Subreddit
from django.utils import timezone

class ValidateSubreddit():
    def __init__(self, request):
        self.request = request

    def create_subreddit(self):
        subreddit = Subreddit() 
        
        subreddit.slug = self.request.POST['slug'] 
        subreddit.avatar = self.request.FILES['avatar']
        subreddit.title = self.request.POST['title'] 
        subreddit.content = self.request.POST['description']
        subreddit.photo = self.request.FILES['photo'] 
        subreddit.pub_date = timezone.datetime.now()
        subreddit.user = self.request.user
        subreddit.subreddit = self.request.subreddit

        subreddit.save() 

        return subreddit

    def is_create_subreddit_valid(self):
        return (
            self.request.method == 'POST' and
            self.request.POST['slug'] and
            self.request.POST['avatar'] and
            self.request.POST['title'] and 
            self.request.POST['description'] and
            self.request.FILES['photo']
        )

    # user
    # slug 
    # avatar
    # title 
    # description 
    # photo 
    # pub_date