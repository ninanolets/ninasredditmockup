from django.db import models
from datetime import datetime

from django.contrib.auth.models import User 


class Subreddit(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    slug = models.SlugField(max_length=30)
    # slug = models.AutoSlugField(populate_from='title', always_update=True)

    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.slug) or ''
    
    def custom_pub_date(self):
        return self.pub_date.strftime('%e %b %Y')