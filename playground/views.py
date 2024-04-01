from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def say_hello(request):
    Product.objects

    return render(request, 'index.html', {'name': 'Rex'})
