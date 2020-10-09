from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from subreddits.models import Subreddit

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=150)
    content = models.TextField(default='') # or blank=True
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
	
    def __str__(self):
        return self.title

    def custom_pub_date(self):
        return self.pub_date.strftime('%e %b %Y')
    
    def custom_title(self):
        if len(self.title) > 40:
            return self.title[:40] + "..." 
        return self.title
    
    

