from django.shortcuts import render


def index(request):
    contex = {
              'title': 'Store',
              }
    return render(request, 'products/index.html', contex)


def products(request):
    return render(request, 'products/products.html')