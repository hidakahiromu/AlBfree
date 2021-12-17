
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.RestaurantsList, name='RestaurantsList'),
    path('storedetails/', views.StoreDetails, name='StoreDetail'),
    # 店舗詳細画面を呼び出す
    path('<int:restaurant_id>', views.DbStoreDetails, name='DbStoreDetail'),
]
