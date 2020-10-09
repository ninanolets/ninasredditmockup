from django.urls import path
from . import views

urlpatterns = [
    path('<int:posts_id>/upvote_comment/<int:comments_id>', views.upvote_comment, name='upvote_comment'), 
]
