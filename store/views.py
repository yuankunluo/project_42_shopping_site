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
    products = Product.objects.all()
    for p in products:
        p.img_url = p.image.url[6:]
    return render(request,'store/product_list.html',
                  {'title':'hello','active':'product','products':products, 'user':request.user})

@require_GET
def product_slug(request, product_slug):
    product = Product.objects.get(slug = product_slug)
    product.img_url = product.image.url[6:]
    categories = product.category.all()
    c = []
    for cn in categories:
        c.append(cn.name)
    return render(request,'store/product_page.html',
                  {'title':'hello','active':'product','product':product,'categories':c, 'user':request.user})



def product_search(request):
    """
    @TODO
    :param request:
    :return:
    """
    search_term = request.POST['search_term']
    products = []
    return HttpResponseRedirect('/product/')


@require_GET
def product_id(request, product_id):
    return render(request,'store/base.html',{'title':'hello','active':'account', 'user':request.user})