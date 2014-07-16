from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
import cart

# Create your views here.

def show_cart(request):
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    return render(request,'cart/cart.html',{'cart_items':cart_items,'cart_subtotal':cart_subtotal})


def add_product_to_cart(request, product_slug):
    cart.add_to_cart(request)
    return HttpResponseRedirect('/cart/')

def update_cart(request):
    cart.update_cart(request)
    return HttpResponseRedirect('/cart/')

def remove_cart(request):
    cart.remove_from_cart(request)
    return HttpResponseRedirect('/cart/')


