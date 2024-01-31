from django.shortcuts import render
from .models import Post
from rest_framework import generics
from django.http import JsonResponse
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListAPIView):
    #get all post, limit=30
    queryset = Post.objects.order_by('created_at').reverse().all()[:30]
    serializer_class=PostSerializer

class PostAdd(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

