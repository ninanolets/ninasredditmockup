from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('post/<int:posts_id>', views.post, name='post'), 
    path('post/create', views.create, name='create'), 
    path('post/delete/<int:posts_id>', views.delete_post, name='delete_post'),
    path('post/', include('comments.urls')),
    path('post/', include('commupvotes.urls')),
    path('post/', include('postupvotes.urls')),
]
