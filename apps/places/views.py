from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from .serializers import PlaceSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PlaceList(generics.ListAPIView):
    # Get all places, limit= 25
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category']
    search_field = ['name', 'description']