from django.urls import path, include
from . import views

urlpatterns = [
    path('s/<slug:slug>/post/<int:posts_id>', views.post, name='post'), 
    path('s/<slug:slug>/post/create', views.create, name='create'), 
    path('post/create', views.create_from_index, name='create_from_index'), 
    path('post/delete/<int:posts_id>', views.delete_post, name='delete_post'),
    path('s/<slug:slug>/post/<int:posts_id>/update_post', views.update_post, name='update_post'),
    path('s/<slug:slug>/post/', include('comments.urls')),
    path('s/<slug:slug>/post/', include('commupvotes.urls')),
    path('post/', include('postupvotes.urls')),
]
