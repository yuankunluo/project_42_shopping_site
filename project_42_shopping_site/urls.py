from django.conf.urls import patterns, include, url

from django.contrib import admin
from store import urls as store_urls
from store import views as store_views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',store_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/',include(store_urls)), # redirect all urls to store
    url(r'^product/$',store_views.product_all,name='product_all'),
)
