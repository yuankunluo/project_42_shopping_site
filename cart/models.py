from django.db import models
from store.models import Product


# Create your models here.
class CartItem(models.Model):
    """
    CartItem table represents the temporary items that being added into cart by user.

    It has
        * an ID to remember it from session and cookies
        * the date it be created
        * the quantity
        * the reference to Product

    """
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False)


    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price()

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price()

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()