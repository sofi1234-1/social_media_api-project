from django.urls import path
from .views import PostListCreateView, PostDetailView, FollowView, UnfollowView, FeedView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('follow/', FollowView.as_view(), name='follow'),
    path('unfollow/', UnfollowView.as_view(), name='unfollow'),
    path('feed/', FeedView.as_view(), name='feed'),
]
