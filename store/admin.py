from django.contrib import admin

# Register your models here.


# ====================
# ProductHasCategory Admin
# ====================
from store.models import ProductHasCategories
class ProductHasCategoryAdmin(admin.TabularInline):
    model = ProductHasCategories
    max_num = 10


# ====================
# Product Admin
# ====================
from store.models import Product
class ProductAdmin(admin.ModelAdmin):
    """
    Using customer admin
    """
    inlines = (ProductHasCategoryAdmin,)
    fieldsets = [
        ('General',{'fields':['product_name','meta_description','meta_keywords','description']}),
        ('Information',{'fields':['manufacturer','brand']}),
        ('Data',{'fields':['model','ean','quantity','price'],}),
        ('Date',{'fields':['date_available','date_import','date_update']}),
        ('Package',{'fields':['dimension_length','dimension_height','dimension_width','weight']}),
        ('On Sale',{'fields':['onsale','sale_price','sale_date_start','sale_date_end']}),
        ('Enable This Product',{'fields':['enable']})
    ]
    list_display = ('product_name','manufacturer','price','enable')



admin.site.register(Product,ProductAdmin)

# ====================
# Manufacturer Admin
# ====================
from store.models import Manufacturer
admin.site.register(Manufacturer)



# ====================
# Category Admin
# ====================
from store.models import Category
admin.site.register(Category)