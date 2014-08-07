from django.shortcuts import render
from store.models import Product
from cart.models import CartItem
from account.models import Order

# Create your views here.


def homepage(request):
    """
    Return the homepage views to the user.
    It contains the product slider, bestseller and statistic informations.

    :param request: The http request
    :return: The html
    """
    featured_products = Product.objects.filter(is_featured=True)
    for p in featured_products:
        p.img_url = p.image.url[6:] # get the url for display
        p.des = p.description[:50]

    p_active = featured_products[0]
    p_items = featured_products[1:]

    products = Product.objects.all()
    for p in products:
        p.img_url = p.image.url[6:] # get the url for display

    # get the selling statistic
    top_list = get_top_selling(3)




    return render(request,'homepage/homepage.html',{'p_items':p_items,'p_active':p_active,
                                                    'products':products, 'top_list':top_list})


def get_top_selling(topn = 5):
    """
    Calculate the top5 selling products all the time.

    :param: The top number
    :return: An OrderedDict of [(Product : selling_quantity)]
    """
    orders = Order.objects.all()
    result = {}

    for o in orders:
        cartId = o.cart_id
        cartItems = CartItem.objects.filter(cart_id = cartId)
        for item in cartItems:
            pId = item.product_id
            pQuan = item.quantity
            if pId not in result.keys():
                result[pId] = pQuan
            else:
                result[pId] = result[pId] + pQuan


    from collections import OrderedDict
    # sort this dict
    result_sorted = OrderedDict(sorted(result.items(), key=lambda x: x[1],reverse=True))

    result_list = []
    for k in result_sorted.keys():
        p = Product.objects.get(id = k)
        result_list.append((p,result_sorted[k]))

    return result_list[:topn]



