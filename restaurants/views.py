from django.shortcuts import render

# Create your views here.
def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def RestaurantsList(request):
    return render(request , 'restaurantsList.html')