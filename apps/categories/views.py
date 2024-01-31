from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]


