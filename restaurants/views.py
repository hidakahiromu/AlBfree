from django.shortcuts import render
from .models import store_information

# Create your views here.
def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def RestaurantsList(request):
    db = {
        'restaurants_db' : store_information.objects.all()
    }
    return render(request , 'restaurantsList.html' , db)