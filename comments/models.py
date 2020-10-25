from django.db import models
from datetime import datetime

from posts.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    post = models.ForeignKey(Post, related_name="commented", on_delete=models.CASCADE)
    # related_name, so you can acess every post's comment (and count) on the template
    # {{ post.commented.count }}
    
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.content) or ''
    


