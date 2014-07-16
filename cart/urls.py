from django.conf.urls import patterns, include, url
import views as cart_views

urlpatterns = patterns('',
    url(r'^$', cart_views.show_cart,name='show_cart'),
    url(r'^add/(?P<product_slug>\S+)/$', cart_views.add_product_to_cart, name='add_product_to_cart'),
    url(r'^update/$',cart_views.update_cart,name='update_cart'),
    url(r'^remove/$',cart_views.remove_cart,name='remove_cart'),
)