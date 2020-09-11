from django.db import models

class Subreddit(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
