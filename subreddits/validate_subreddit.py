from .models import Subreddit
from django.utils import timezone
import re

class ValidateSubreddit():
    def __init__(self, request):
        self.request = request

    def create_subreddit(self):
        subreddit = Subreddit() 

        subreddit.slug = re.sub('[^a-zA-Z0-9\.]', '_', self.request.POST['slug'])
        
        subreddit.title = self.request.POST['title'] 
        subreddit.description = self.request.POST['content']
        subreddit.photo = self.request.FILES['photo'] 
        
        try:
            subreddit.avatar = self.request.FILES['avatar']
        except:
            subreddit.avatar = self.request.POST.get('avatar', False)

        subreddit.pub_date = timezone.datetime.now()
        subreddit.user = self.request.user

        subreddit.save() 

        return subreddit

    def is_create_subreddit_valid(self):
        return (
            self.request.POST['slug'] and
            self.request.POST['title'] and 
            self.request.POST['content'] and
            self.request.FILES['photo']
        )

    # user
    # slug 
    # avatar
    # title 
    # description 
    # photo 
    # pub_date