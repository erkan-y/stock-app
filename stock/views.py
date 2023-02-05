from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import *
from .serializers import *

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
