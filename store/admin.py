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

admin.site.register(Product,ProductAdmin)



# ====================
# Category Admin
# ====================
from store.models import Category
admin.site.register(Category)

# ====================
# Brand Admin
# ====================
from store.models import Brand
admin.site.register(Brand)