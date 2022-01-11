
from django.urls import path
from . import views



urlpatterns = [
    path('storedetails/', views.StoreDetails, name='StoreDetail'),
    path('list/', views.RestaurantsList, name='RestaurantsList'),
    path('restaurantimageform/' , views.RestaurantImageForm , name="RestaurantImageForm"),
    path('restaurantsform/' , views.RestaurantsForm , name='RestaurantsForm'),
    path('restaurantmenuform/' , views.RestaurantMenuForm , name='RestaurantMenuForm'),
]
