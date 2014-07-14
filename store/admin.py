from django.contrib import admin

# Register your models here.


#==========================================================================
# ProductHasCategoryAdmin
#==========================================================================
from store.models import ProductHasCategories
class ProductHasCategoryAdmin(admin.TabularInline):
    model = ProductHasCategories
    max_num = 10

#==========================================================================
# ProductAdmin
#==========================================================================
from store.models import Product
from store.forms import ProductAdminForm
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # sets values for how the admin site lists your products
    list_display = ('name', 'onsale_price', 'default_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug':('name',), 'onsale_price':('default_price',),
                           'image_caption':('slug',)}
    inlines = [ProductHasCategoryAdmin,]
admin.site.register(Product,ProductAdmin)

#==========================================================================
# Category Admin
#==========================================================================
from store.models import Category
class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

#==========================================================================
# Brand Admin
#==========================================================================
from store.models import Brand
class Branddmin(admin.ModelAdmin):
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Brand, Branddmin)