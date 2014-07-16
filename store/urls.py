from django.conf.urls import patterns, include, url
from store import views

urlpatterns = patterns('',
    url(r'^product/$', views.product_all, name='index'),
    url(r'^product/(?P<product_slug>\S+)/$',views.product_slug, name='product_slug'),
)