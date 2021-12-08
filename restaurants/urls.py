from django.urls import path
from . import views

urlpatterns = [
    path('shopdetails/', views.ShopDetails, name='ShopDetail')
]
