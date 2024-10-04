from rest_framework import generics, permissions
from .models import Post, Follow
from .serializers import PostSerializer, FollowSerializer
from django.contrib.auth.models import User
from django.shortcuts import render 
   

# CRUD views for posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

# Follow and Unfollow functionality
class FollowView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class UnfollowView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

# Feed of followed posts
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_ids = self.request.user.following.values_list('following_id', flat=True)
        return Post.objects.filter(user_id__in=following_ids).order_by('-timestamp')
