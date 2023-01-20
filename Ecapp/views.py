from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def allprodcat(request, C_slug=None):
    c_page = None
    products_list = None
    if C_slug != None:
        c_page = get_object_or_404(category, slug=C_slug)
        products_list = product.objects.all().filter(category=c_page, avilable=True)
    else:
        products_list = product.objects.all().filter(avilable=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products})


def prodetail(request, C_slug, product_slug):
    try:
        Product = product.objects.get(category__slug=C_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': Product})
