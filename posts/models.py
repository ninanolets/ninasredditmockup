from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from subreddits.models import Subreddit

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    subreddit = models.ForeignKey(Subreddit, related_name="sub_posts", on_delete=models.CASCADE)
    
    title = models.CharField(max_length=150)
    content = models.TextField(default='') # or blank=True
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.title) or ''

    def custom_pub_date(self):
        return self.pub_date.strftime('%e %b %Y')
    
    def compare_pub_date(self):
        return self.pub_date.strftime('%e %b %Y %H %M %S')    
    def compare_update_date(self):
        return self.update_date.strftime('%e %b %Y %H %M %S')
    
    def custom_title(self):
        if len(self.title) > 40:
            return self.title[:40] + "..." 
        return self.title
    
    
    
    

