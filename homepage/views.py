from django.shortcuts import render
from store.models import Product

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

    return render(request,'homepage/homepage.html',{'p_items':p_items,'p_active':p_active,
                                                    'products':products})