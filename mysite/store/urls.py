from django.urls import path
from  .views import  ProductViewSet
urlpatterns=[
    path('',ProductViewSet.as_view({'get':'list'}),name ='product_list')
]