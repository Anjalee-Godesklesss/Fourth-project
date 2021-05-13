from django.shortcuts import render
from .models import Listing
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings=Listing.order_by('_list_date').filter(is_published=True)[:3]
    context ={
        'listings': listings
    }
    return render(request,'pages/base.html',context)


def index(request):
    return render(request, 'listings/listings.html',{'name':'Brad'})

def listing(request):
    return render(request,'listings/search.html')

def search(request):
    return render(request, 'listings/search.html')
# Create your views here.

def about(request):
    realtors = Realtor.objects.order_by('_hire_date')
    return render(request, 'pages/about.html')
