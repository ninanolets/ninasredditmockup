from django.urls import path
from . import views

urlpatterns = [
	path('<int:subreddits_id>', views.subreddit, name='subreddit'), 
	path('all_subreddits', views.all_subreddits, name='all_subreddits'),
	path('create', views.create, name='create_sub'),
	path('delete/<int:subreddits_id>', views.delete_sub, name='delete_sub'),
]