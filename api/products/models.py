from django.db import models
import cloudinary
import cloudinary.models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = cloudinary.models.CloudinaryField('image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")  # Link to Category
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
