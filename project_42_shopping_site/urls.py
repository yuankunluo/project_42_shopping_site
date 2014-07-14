from django.conf.urls import patterns, include, url

from django.contrib import admin
from store import urls as store_urls


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_42_shopping_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$",include(store_urls)), # redirect all urls to store
)
