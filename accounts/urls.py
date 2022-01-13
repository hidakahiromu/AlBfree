from django.urls import path
from . import views

urlpatterns = [
 #http://127.0.0.1:8000/XXX/
    path('', views.TopPage, name='TopPage'),    #トップページ
    #path('storedetails/', views.StoreDetails, name='StoreDetails'),  #店舗詳細
    path('registration/' , views.registration , name='registration'),   #アカウント新規作成
    path('terms/' , views.terms , name='terms'), #利用規約
    path('forstores/' , views.forstores , name='forstores'), #店舗向け案内
    path('login/', views.login ,name='login'),   #ログイン画面
]