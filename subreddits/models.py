from django.db import models
from django.contrib.auth.models import User 

class Subreddit(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=40)
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.slug
