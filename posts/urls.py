from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('<int:posts_id>', views.post, name='post'), 
    path('create', views.create, name='create'), 
]
