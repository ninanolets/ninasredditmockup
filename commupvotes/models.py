from django.db import models

from comments.models import Comment
from django.contrib.auth.models import User

class Commupvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, related_name="upvotes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
