from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:post_pk>/comments/new/', views.comment_create, name='comment_create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/', views.comment_update, name='comment_update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('signup/', views.signup, name='signup'),
]