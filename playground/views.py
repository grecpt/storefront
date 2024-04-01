from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def say_hello(request):
    query_set = Product.objects.all()
    query_set.filter().filter().order_by()

    return render(request, 'index.html', {'name': 'Rex'})
