from django.db import models

# Create your models here.




class Manufacturer(models.Model):
    """
    The Manufacturer of products:

    Attributes:
    name    The name of manufacturer
    location    The location of this manufacturer
    description The description of this manufacturer
    """
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return "[Manufacturer]: " + self.name


class Category(models.Model):
    """
    The category of a product:

    Attributes:
    name    Category name
    meta_description    Html meta tag
    meta_keywords   Html meta tag
    description  Description
    parent  The parent category
    top The token, if it the top category
    """
    name = models.CharField(max_length=200)
    meta_description = models.TextField(max_length=500)
    meta_keywords = models.TextField(max_length=500)
    description = models.TextField(max_length=10000)
    parent = models.ForeignKey("self")
    top = models.BooleanField(default=False)

    def __unicode__(self):
        return "[Category]: " + self.name

class Image(models.Model):
    pass

class Product(models.Model):
    """
    The class presents the Product.

    Every Product has the following attributes:

    Attributes:

    product_name    The name of product in system
    meta_description   The description that displayed in html meta tag
    meta_description    The keywords that displayed in html meta tag
    description The html description of this product
    model   The model of product
    ean European Article Number
    price The price
    quantity The quantity in stock
    date_available  The avaliable date of this product
    date_import The date this product imported into system
    date_update The last update time
    dimension_length The dimension
    dimension_height The dimension
    dimension_width The dimension
    weight  The weight
    manufacturer    The manufacturer
    """

    product_name = models.CharField(max_length=200)
    meta_description = models.TextField(max_length=1000)
    meta_keywords = models.TextField(max_length=1000)
    description = models.TextField(max_length=100000)
    model = models.CharField(max_length=200)
    ean = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    date_available = models.DateField()
    date_import = models.DateTimeField()
    date_update = models.DateTimeField()
    dimension_length = models.FloatField()
    dimension_height = models.FloatField()
    dimension_width = models.FloatField()
    weight = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "[Product]: " + self.product_name
