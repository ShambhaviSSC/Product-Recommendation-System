from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Product
from realtors.models import Seller
from listings.choices import price_choices,type_choices,brand_choices


# Create your views here.
def index(request):
    listings = Product.objects.order_by('-list_date').filter(is_available=True)[:3]

    context = {
        'listings' : listings,
        'price_choices': price_choices,
        'brand_choices': brand_choices,
        'type_choices': type_choices,
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Seller.objects.order_by('-contract_date')

    mvp_realtors = Seller.objects.all().filter(is_top=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html',context)