from django.shortcuts import render
from .models import store_information

from accounts.models import user_information

# Create your views here.
def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def RestaurantsList(request):
    db = {
        'restaurants_db' : store_information.objects.all(),
        'user_db' : store_information.objects.get(restaurant_id_id = 0)
    }
    return render(request , 'restaurantsList.html' , db)