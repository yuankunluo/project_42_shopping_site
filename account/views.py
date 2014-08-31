from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from cart import cart as cart_module
from cart.models import CartItem
from models import Order

# Create your views here.

CART_ID_SESSION_KEY = 'cart_id'

@login_required(login_url='/account/login/')
def account(request):
    """
    Using the login function of django to determin the user if he want to see the account page.

    :param request: http request
    :return: if authenticated user, then return the account page, else redirect him to login page.
    """
    if request.user.is_authenticated():
        # Do something for authenticated users.
        orders = Order.objects.filter(username = request.user.username)
        return render(request, 'account/account.html', {'user': request.user, 'orders':orders})
    else:
        return HttpResponseRedirect('/account/login/')


def register(request):
    """
    Using the information form request to register user.

    It check the password 1 and password 2 that were given by user,
    if p1 != p2, then give the error as response.

    Adding a user with the django if all information was fine.


    :param request: request
    :return: response
    """
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if request.method == 'POST':
        u = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        e = request.POST['email']
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        if p1 != p2:
            return render(request, 'account/error.html', {'error': 'Password were not the same'})
        request.session.flush()
        user = User.objects.create_user(u, e, p1)
        user.first_name = fn
        user.last_name = ln
        user.is_active = True
        user.save()
        user = authenticate(username=u, password=p1)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def do_login(request):
    """
    Get the username and password from request as the arguments of authenticate() function by django,
    to detect if this user is active.

    :param request: request
    :return: respones
    """
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        request.session.flush()
        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/account/')
        else:
           return HttpResponseRedirect('/')



@login_required(login_url='/account/login/')
def order(request):
    return HttpResponseRedirect('/account/')

@login_required(login_url='/account/login/')
def order_detail(request, order_id):
    order = Order.objects.filter(order_id = order_id)[0]
    cart_id = order.cart_id
    cart_items = CartItem.objects.filter(cart_id=order.cart_id)
    return render(request,'account/order.html', {'order':order, 'cart_items':cart_items})




@login_required(login_url='/account/login/')
def checkout(request):
    if request.method == 'POST':
        cart_items = cart_module.get_cart_items(request)
        cart_subtotal = cart_module.cart_subtotal(request)
        return render(request, 'account/checkout.html', {'cart_items':cart_items,
                                            'cart_id':cart_items[0].cart_id,
                                            'cart_subtotal':cart_subtotal, 'user':request.user} )
    else:
        return HttpResponseRedirect('/account/')



@login_required(login_url='/account/login/')
def pay(request):
    """
    Do the "create order" thing.
    It get the CARD_ID_SESSION_KEY from session to get the items information that been added into cart by user.
    Then calling the cart_subtotal() function in cart_module to get the order total price.

    The shipping information will also be collected through html form.

    If every thing is fine, then create an order, else return error message.

    :param request:
    :return:
    """
    if request.method == 'POST':
        if request.session[CART_ID_SESSION_KEY] != '':
            cart_items = cart_module.get_cart_items(request)
            cart_subtotal = cart_module.cart_subtotal(request)
            shipping_zip = request.POST['shipping_zip']
            shipping_add = request.POST['shipping_add']
            shipping_to = request.POST['shipping_to']
            username = request.user.username
            cart_id = cart_items[0].cart_id

            try:
                order = Order.objects.get(cart_id = request.session[CART_ID_SESSION_KEY])
            except Order.DoesNotExist:
                order = None

            if order != None:
                order = Order.objects.get(cart_id=request.session[CART_ID_SESSION_KEY])
            else:
                order = Order()

            order.cart_id = cart_id
            order.shipping_add = shipping_add
            order.shipping_to = shipping_to
            order.shipping_zip = shipping_zip
            order.username = username
            order.total_price = cart_subtotal
            order.save()
            request.session[CART_ID_SESSION_KEY] = '' # delete session key
            return HttpResponseRedirect('/account/order/'+order.order_id+'/')
        else:
            return render(request, 'account/error.html',{'error':'This order has been created.' })
    else:
        return HttpResponseRedirect('/account/')


