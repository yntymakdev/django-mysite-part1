
from django.contrib import admin

from store.models import Category, Product,Comment,ProductPhotos

# Register your models here.
admin.site.register(Category)
admin.site.register(Product),
admin.site.register(Comment)
admin.site.register(ProductPhotos)
