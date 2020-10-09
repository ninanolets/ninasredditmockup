from django.urls import path
from . import views

urlpatterns = [
    path('<int:posts_id>/upvote_post', views.upvote_post, name='upvote_post'), 
]
