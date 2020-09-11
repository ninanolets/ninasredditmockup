from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='subreddits'),
	# path('<int:subreddits_id>', views.subreddit, name='subreddit'), 
	# path('search', views.search, name='search'),
]