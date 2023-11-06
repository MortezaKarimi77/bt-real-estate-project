from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import *


def listings(request):
    listings = Listing.objects.filter(
        is_published=True).order_by('-listed_date')

    # pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(listings, 3)
    page = paginator.get_page(page_number)
    last_page_number = paginator.num_pages
    current_page_number = page.number
    other_pages = page.has_other_pages()
    ellipsis = paginator.ELLIPSIS
    page_range = paginator.get_elided_page_range(
        page_number, on_each_side=1, on_ends=1
    )

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
        'listings_active': 'active',
        'title': 'املاک ویژه',
        'listings': page,
        'page_range': page_range,
        'prev_url': prev_url,
        'next_url': next_url,
        'other_pages': other_pages,
        'last_page_number': last_page_number,
        'current_page_number': current_page_number,
        'ellipsis': ellipsis,
        'state_choices': state_choices,
        'message': 'در حال حاضر چیزی وجود ندارد'
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return_url = request.META['QUERY_STRING'].lstrip('back=')

    context = {
        'listings_active': 'active',
        'title': listing.title,
        'listing': listing,
        'return_url': return_url,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    # search terms
    found_items = Listing.objects.order_by('-listed_date')

    start = request.META['QUERY_STRING'].index('&')
    query_string = request.META['QUERY_STRING'][start:]

    if request.GET.get('bedrooms'):
        searched_bedrooms = request.GET['bedrooms']
        request.session['searched_bedrooms'] = searched_bedrooms
        found_items = found_items.filter(bedrooms__lte=searched_bedrooms)

    if request.GET.get('price'):
        searched_price = request.GET['price']
        request.session['searched_price'] = searched_price

        if int(searched_price) >= 1000000:
            found_items = found_items.filter(price__gte=searched_price)
        else:
            found_items = found_items.filter(price__lte=searched_price)

    if request.GET.get('state'):
        searched_state = request.GET['state']
        request.session['searched_state'] = searched_state
        found_items = found_items.filter(state=searched_state)

    if request.GET.get('keywords'):
        searched_keywords = request.GET['keywords']
        request.session['searched_keywords'] = searched_keywords
        found_items = found_items.filter(
            descriptions__icontains=searched_keywords
        )

    if request.GET.get('city'):
        searched_city = request.GET['city']
        request.session['searched_city'] = searched_city
        found_items = found_items.filter(city=searched_city)

    # pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(found_items, 3)
    page = paginator.get_page(page_number)
    last_page_number = paginator.num_pages
    current_page_number = page.number
    other_pages = page.has_other_pages()
    ellipsis = paginator.ELLIPSIS
    page_range = paginator.get_elided_page_range(
        page_number, on_each_side=1, on_ends=1
    )

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}' + query_string
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}' + query_string
    else:
        next_url = ''

    context = {
        'listings_active': 'active',
        'title': 'جستجو در لیست املاک',
        'message': 'موردی یافت نشد',
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'search_terms': request.GET,
        'query_string': query_string,
        'listings': page,
        'next_url': next_url,
        'prev_url': prev_url,
        'last_page_number': last_page_number,
        'current_page_number': current_page_number,
        'other_pages': other_pages,
        'ellipsis': ellipsis,
        'page_range': page_range
    }

    return render(request, 'listings/search.html', context)
