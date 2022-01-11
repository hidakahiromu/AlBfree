
from django.urls import path
from . import views

urlpatterns = [
    path('storedetails/', views.StoreDetails, name='StoreDetail'),
    path('list/', views.RestaurantsList, name='RestaurantsList'),
    path('modelForm/' , views.Form , name="Form"),
]
