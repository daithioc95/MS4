from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product
from .forms import ProductForm


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
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
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

    current_sorting = f'{sort}-{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_period': period,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def all_artists(request):
    period = None
    edo_artists = {}
    meiji_artists = {}
    other_artists = {}
    for x in Product.objects.all():
        try:
            if x.Artist_Display_Name not in edo_artists:
                if x.Period == "Edo period (1615–1868)":
                    edo_artists.update({x.Artist_Display_Name: x.image.url})
            if x.Artist_Display_Name not in meiji_artists:
                if x.Period == "Meiji period (1868–1912)":
                    meiji_artists.update({x.Artist_Display_Name: x.image.url})
            if x.Artist_Display_Name not in other_artists:
                if x.Period != "Edo period (1615–1868)":
                    if x.Period != "Meiji period (1868–1912)":
                        if x.Artist_Display_Name and x.image.url:
                            other_artists.update(
                                {x.Artist_Display_Name: x.image.url}
                                )
        except:
            pass
    if 'Period' in request.GET:
            period = request.GET['Period']

    context = {
        'edo_artists': edo_artists,
        'meiji_artists': meiji_artists,
        'period': period,
        'other_artists': other_artists,
    }

    return render(request, 'products/artists.html', context)


def artist_detail(request, artist_name):
    products = Product.objects.all().filter(Artist_Display_Name=artist_name)

    similar_artists = {}
    try:
        for x in Product.objects.all():
            for y in products:
                if x.Period == y.Period:
                    if x.Artist_Display_Name != y.Artist_Display_Name:
                        if len(similar_artists) < 3:
                            similar_artists.update(
                                {x.Artist_Display_Name: x.image.url}
                                )
    except:
        pass

    context = {
        'products': products,
        'artist': artist_name,
        'similar_artists': similar_artists,
    }

    return render(request, 'products/artist_detail.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    other_products = Product.objects.all().filter(
                                Artist_Display_Name=product.Artist_Display_Name
                                )

    context = {
        'product': product,
        'other_products': other_products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                    request,
                    'Failed to update product. Please ensure the form is valid.'
                        )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
