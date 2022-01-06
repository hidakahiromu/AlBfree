from django.urls import path
from . import views
#from django.contrib.auth.views import logout

urlpatterns = [
    path('templates/', views.index_template, name='index_template'),
    path('toppage', views.TopPage, name='TopPage'),
    path('shopdetails/', views.ShopDetails, name='ShopDetails'),
    path('service/' , views.service , name='service'),
    #認証機能関連
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]
