from django.conf.urls import patterns, include, url
import views as account_views
from project_42_shopping_site import settings

urlpatterns = patterns('',
                       url(r'^$', account_views.account, name='account_index'),
                       url(r'^login/$',account_views.do_login),
                       url(r'^logout/$',account_views.do_logout),
                       url(r'^order/$',account_views.order),
                       url(r'^register/$', account_views.register, name='register'),
                       url(r'^checkout/$', account_views.checkout, name='checkout'),
                       url(r'^pay/$',account_views.pay, name='pay'),
                       url(r'^order/(?P<order_id>\S+)/$', account_views.order_detail, name='order_detail'),
)
