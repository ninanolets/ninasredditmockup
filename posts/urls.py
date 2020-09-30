from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('post/<int:posts_id>', views.post, name='post'), 
    path('post/create', views.create, name='create'), 
]
