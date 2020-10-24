from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('s/<slug:slug>', views.subreddit, name='subreddit'), 
	path('', include('posts.urls')),
	path('all_subreddits', views.all_subreddits, name='all_subreddits'),
	path('create_sub', views.create, name='create_sub'),
	path('s/<slug:slug>/update_sub', views.update_sub, name='update_sub'),
	path('delete_sub/<int:subreddits_id>', views.delete_sub, name='delete_sub'),
]

