from django.db import models

from posts.models import Post
from django.contrib.auth.models import User

class Postupvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name="upvotes", on_delete=models.CASCADE)
    # {{ post.upvotes }}

    def __str__(self):
        return str(self.id)

    
    
