from django.contrib import admin

# Register your models here.

# ====================
# Product Admin
# ====================
from hylee_beauty.models import Product

class ProductAdmin(admin.ModelAdmin):
    """
    Using customer admin
    """
    fieldsets = [
        ('General',{'fields':['product_name','meta_description','meta_keywords','description']}),
        ('Information',{'fields':['manufacturer','brand','category']}),
        ('Data',{'fields':['model','ean','quantity','price'],}),
        ('Date',{'fields':['date_available','date_import','date_update']}),
        ('Package',{'fields':['dimension_length','dimension_height','dimension_width','weight']}),
        ('On Sale',{'fields':['onsale','sale_price','sale_date_start','sale_date_end']}),
        ('Enable This Product',{'fields':['enabel']})
    ]


admin.site.register(Product,ProductAdmin)