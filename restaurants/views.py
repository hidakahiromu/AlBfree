from django.shortcuts import render
from .models import store_information

# Create your views here.


def ShopDetails(request):
    return render(request, 'StoreDetails.html')


def RestaurantsList(request):
    db = {
        'test_list': store_information.objects.all()
    }
    return render(request, 'restaurantsList.html', db)
