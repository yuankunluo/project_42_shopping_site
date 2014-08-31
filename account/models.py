from django.db import models
import random
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    """
    Username is the unique token in auth system,
    so we use username to denote user's order

    """
    username = models.CharField(max_length=200)
    cart_id = models.CharField(max_length=50)

    total_price = models.DecimalField(max_digits=9,decimal_places=2, blank=False,default=0.00)
    shipping_to = models.CharField(max_length=200)
    shipping_add = models.CharField(max_length=200)
    shipping_zip = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    order_id = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        self.order_id = self.generateID()
        super(Order, self).save(*args, **kwargs) # Call the "real" save() method.


    def generateID(self):
        """
        Automatically generate an ID for every order, starts with 'ORD-' following by the randomly numbers.

        :return: String as ID
        """
        oid = 'ORD-5'
        characters = '0123456789'
        for y in range(15):
            oid += characters[random.randint(0, len(characters)-1)]
        return oid


    class Meta:
        ordering = ['created_at']

    def __unicode__(self):
        return self.order_id


