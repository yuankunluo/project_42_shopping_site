from django.conf.urls import patterns, include, url
import views as account_views

urlpatterns = patterns('',
    url(r'^/$', account_views.account_index(),name='show_cart'),

)