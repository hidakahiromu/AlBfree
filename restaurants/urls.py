
from django.urls import path
from . import views



urlpatterns = [
    #http://127.0.0.1:8000/restaurants/XXX/
    path('storedetails/', views.StoreDetails, name='StoreDetail'),  #店舗詳細
    path('restaurantslist/', views.RestaurantsList, name='RestaurantsList'),    #店舗一覧
    path('restaurantimageform/' , views.RestaurantImageForm , name="RestaurantImageForm"),  #画像登録
    path('restaurantsform/' , views.RestaurantsForm , name='RestaurantsForm'),  #飲食店登録
    path('restaurantmenuform/' , views.RestaurantMenuForm , name='RestaurantMenuForm'), #メニュー登録
    path('restaurantreviewform/' , views.RestaurantReviewForm , name='RestaurantReviewForm'),  #レビュー登録 
    path('customerquestionform/' , views.CustomerQuestionForm , name='CustomerQuestionForm'),   #カスタマーQ&A回答フォーム
    path('customeranswerform/' , views.CustomerAnswerForm , name='CustomerAnswerForm'), #カスタマーQ&A回答フォーム
    path('confirmation/' , views.confirmation , name='confirmation') #完了画面
]
