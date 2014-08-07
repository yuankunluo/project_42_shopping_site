from django.shortcuts import render

# Create your views here.


def homepage(request):
    """
    Return the homepage views to the user.
    It contains the product slider, bestseller and statistic informations.

    :param request: The http request
    :return: The html
    """
    return render(request,'homepage/homepage.html')