from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    have=models.BooleanField(default=False)
    video=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.product_name
class  ProductPhotos(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='img/')
