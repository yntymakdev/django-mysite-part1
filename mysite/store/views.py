from rest_framework import viewsets

from store.models import ProductPhotos
from    .serialaizers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer