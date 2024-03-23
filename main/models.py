from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/product',null=True, blank=True)
    product_category = models.ForeignKey('Category',related_name='product_category',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) # TODO
    
class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.cat_name) # TODO