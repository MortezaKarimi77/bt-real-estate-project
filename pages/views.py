from django.shortcuts import render
from listings.models import Listing
from listings.choices import *
from realtors.models import Realtor


def home(request):
    latest_listings = Listing.objects.filter(
        is_published=True).order_by('-listed_date')[:3]

    context = {
        'home_active': 'active',
        'title': 'صفحه اصلی',
        'latest_listings': latest_listings,
        'message': 'در حال حاضر چیزی وجود ندارد',
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }

    return render(request, 'pages/home.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'about_active': 'active',
        'title': 'درباره ما',
        'message': 'در حال حاضر مشاور املاکی وجود ندارد',
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, 'pages/about.html', context)
