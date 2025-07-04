from rest_framework import viewsets
from .filters import ProductFilter
from store.models import ProductPhotos
from    .serialaizers import *
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import  SearchFilter
class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class =ProductFilter
    search_fields = ['product_name']
