from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    period = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(Artist_Display_Name__icontains=query) | Q(Medium__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'Period' in request.GET:
            period = request.GET['Period']
            if period == "edo":
                period_search = "Edo period (1615–1868)"
                products = products.filter(Period=period_search)
            if period == "meiji":
                period_search = "Meiji period (1868–1912)"
                products = products.filter(Period=period_search)
            if period == "taisho":
                period_search = "Taishō period (1912–26)"
                products = products.filter(Period=period_search)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_period': period,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

# Try boutique ado category approach

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)