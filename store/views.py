from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.http import HttpResponse


# Create your views here.


#==========================================================================
# Index
#==========================================================================
def index(request):

    return render(request,'store/base.html',{'title':'hello','active':'account'})