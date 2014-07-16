from django.conf.urls import patterns, include, url
import views as account_views
from project_42_shopping_site import settings

urlpatterns = patterns('',
    url(r'^$', account_views.account_index,name='account_index'),
    url(r'^register/$', account_views.register, name='register'),
    url(r'^my_account/$', account_views.my_account, name='mu_account'),
    url(r'^order/(?P<order_id>\d+)/$', account_views.order_detail, name='order_detail'),
)

urlpatterns += patterns('django.contrib.auth.views',
                        (r'^login/$', 'login',
                         {'template_name': 'registration/login.html', 'SSL':False }, 'login'),
)