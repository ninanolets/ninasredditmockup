from django.urls import path
from . import views

urlpatterns = [
	path('<int:subreddits_id>', views.subreddit, name='subreddit'), 
	path('create', views.create, name='create_sub'),
]