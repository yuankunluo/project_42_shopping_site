from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST


# Create your views here.


def homepage():
    html = """
        <img scr="{% static "image/404.jpg" %}">
    """
    render(html)
