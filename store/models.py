from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.
#==========================================================================
# Brand
#==========================================================================
class Brand(models.Model):
    """
    Brand
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    # keywords for SEO
    meta_keywords = models.CharField("Meta Keyword",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    # description for SEO
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    description = models.TextField(max_length=10000)

    class Meta:
        db_table = 'brands'
        ordering = ['name']  # order by name A-Z
        verbose_name_plural = 'Brands'

    @models.permalink
    def get_absolute_url(self):
        """
        Return the better url (slug for this product, it helps for SEO)
        """
        return ('brand', (), { 'brand_slug': self.slug })

    def __unicode__(self):
        return self.name

#==========================================================================
# Category
#==========================================================================
class Category(models.Model):
    """
    The Product ORM
    """

    # product name
    name = models.CharField(max_length=50)
    # slug for better url
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    # description
    description = models.TextField()
    # keywords for SEO
    meta_keywords = models.CharField("Meta Keyword",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    # description for SEO
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    # the dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['name']  # order by name A-Z
        verbose_name_plural = 'Categories'

    @models.permalink
    def get_absolute_url(self):
        """
        Return the better url (slug for this product, it helps for SEO)
        """
        return ('category', (), { 'category_slug': self.slug })

    def __unicode__(self):
        return self.name

#==========================================================================
# Product
#==========================================================================
class Product(models.Model):
    """
    The Product ORM
    """

    # product name
    name = models.CharField(max_length=50)
    # slug for better url
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    # keywords for SEO
    meta_keywords = models.CharField("Meta Keyword",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    # description for SEO
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    # description
    description = models.TextField()
    # brand
    brand = models.ForeignKey(Brand)
    # SKU code
    sku = models.CharField(max_length=50, null=True,
                           help_text='The unique SKU Code for every production')
    # ASIN code
    asin = models.CharField(max_length=50, null=True,
                            help_text='The unique ASIN Code for product in USA')
    # EAN code
    ean = models.CharField(max_length=50, null=True,
                            help_text='The unique EAN Code for product in Europe')
    # quantity in stock
    quantity = models.IntegerField()

    # prices & default price
    # With a max_digits value of 9, and decimal_places value of 2,
    # we store values with 2 decimal places,
    # and up to 7 digits to the left of the decimal point.
    # That means our products can be up to $9,999,999.99
    onsale_price = models.DecimalField(max_digits=9,decimal_places=2, help_text='The price will be computeted in order, if it onsale')
    default_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)

    # tokens
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)

    # category
    category = models.ManyToManyField(Category, through='ProductHasCategories')

    # the dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name_plural = 'Products'

    @models.permalink
    def get_absolute_url(self):
        """
        Return the better url (slug for this product, it helps for SEO)
        """
        return ('product', (), { 'product_slug': self.slug })

    def get_price(self):
        """
        Using the token is_onsale to determine if this product is in SALES,

        :returns : The price of integer
        """
        if self.is_onsale:
            return self.onsale_price
        else:
            return self.default_price

    def __unicode__(self):
        return self.name


#==========================================================================
# ProductHasCategories
#==========================================================================
class ProductHasCategories(models.Model):
    """
    This present the relation many to many from Product and Category
    """
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)



