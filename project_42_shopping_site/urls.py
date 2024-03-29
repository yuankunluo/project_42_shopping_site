from django.conf.urls import patterns, include, url

from django.contrib import admin
from store import urls as store_urls
from store import views as store_views
from django.contrib.auth import urls as auth_url
from account import urls as account_urls
from homepage import views as homepageviews
from cart import urls as cart_urls



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',homepageviews.homepage,),# redirect to homepage
    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', include(store_urls)),# redirect all urls to store
    url(r'^product/$', store_views.product_all),
    url(r'^account/', include(account_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^about/$',homepageviews.about,), # the about page
)
