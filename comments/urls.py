from django.urls import path
from . import views

urlpatterns = [
    path('<int:posts_id>/commented', views.create_comment, name='create_comment'), 
    path('<int:comment_post>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'), 
]