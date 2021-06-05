from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {'listings': listings, 'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices}
    if 'message' in request.GET:
        context['message']=request.GET['message']
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all()
    # Get mvp
    mvp_realtors = realtors.filter(is_mvp=True)
    context = {'realtors': realtors, 'mvp_realtors': mvp_realtors}
    return render(request, 'pages/about.html', context)
