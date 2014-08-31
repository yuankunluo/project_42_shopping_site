from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http.response import HttpResponseRedirect
from store.models import Product


# Create your views here.


#==========================================================================
# Index
#==========================================================================
def index(request):
    return HttpResponseRedirect('/product/')

#==========================================================================
# Product
#==========================================================================
@require_GET
def product_all(request):
    """
    Returning all products objects in db.

    :param request: the http request
    :return: the http response
    """
    products = Product.objects.all()
    for p in products:
        p.img_url = p.image.url[6:]
    return render(request,'store/product_list.html',
                  {'title':'hello','active':'product','products':products, 'user':request.user})

@require_GET
def product_slug(request, product_slug):
    """
    If the request is asking for a product slug,
    then it means to find that product page.

    The product_slug in url will be treated as an argument to select record in db.
    The result will be returned.


    :param request: http request
    :param product_slug:  the slug of product
    :return: the http response
    """
    product = Product.objects.get(slug = product_slug)
    product.img_url = product.image.url[6:]
    categories = product.category.all()
    c = []
    for cn in categories:
        c.append(cn.name)
    return render(request,'store/product_page.html',
                  {'title':'hello','active':'product','product':product,'categories':c, 'user':request.user})


@require_POST
def product_search(request):
    """
    Only search for name and description.

    Using the search term from the request to search the relevant products.
    Calling __dict__ inter methode on the Product class,
    then using 'name', 'keywords','description' to select information we need.

    Then we use the ***re module*** to get the regular expression to work.
    Compile the search term as a pattern, then using this pattern to match.

    If matching successfully, then this Product will be collected in a list as result.


    :param request: the search term, get from the request
    :return: the search results
    """
    import re
    search_term = request.POST['search_term'].lower()
    s_pattern = re.compile(search_term)
    products = Product.objects.all()
    keys = ['meta_description', 'meta_keywords', 'name', 'description']
    results = []
    for p in products:
        p.img_url = p.image.url[6:]
        string = ''
        for k in keys:
            string += p.__dict__[k] # get all information
        string = string.lower() # make it lowercase
        finds = re.findall(s_pattern, string)
        if len(finds) != 0:
            results.append(p)
            continue

    return render(request,'store/search_result.html',{'search_term':search_term,'results':results})


@require_GET
def product_id(request, product_id):
    return render(request,'store/base.html',{'title':'hello','active':'account', 'user':request.user})