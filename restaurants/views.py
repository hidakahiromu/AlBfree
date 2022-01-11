from django.shortcuts import render , redirect
from django.conf import settings
from .forms import restaurantInformationForm , restaurantImagesForm , restaurantMenusForm
from .models import restaurant_information , images , menus


# Create your views here.

#飲食店詳細画面
def StoreDetails(request):
    return render(request, 'StoreDetails.html')

#飲食店一覧画面
def RestaurantsList(request):
    db = {
        'restaurants_db' : information.objects.all(),
        #'user_db' : store_information.objects.get(contributor = 0),
    }
    return render(request , 'restaurantsList.html' , db)

#飲食店の情報投稿フォーム
def RestaurantsForm(request):
    if request.method == 'POST':
        form = restaurantInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RestaurantsForm')
    else:
        form = restaurantInformationForm()
    

    return render(request, 'restaurantsInformationForm.html', {
        'form': form
    })

#飲食店のメニュー投稿フォーム
def RestaurantMenuForm(request):
    if request.method == 'POST':
        form = restaurantMenusForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('RestaurantMenuForm')
    else:
        form = restaurantMenusForm()
    

    return render(request, 'restaurantMenusForm.html', {
        'form': form
    })

#飲食店の画像(飲食店のトップ画像など)投稿フォーム　※後で関数名は変えるかも
def RestaurantImageForm(request):
    if request.method == 'POST':
        form = restaurantImagesForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('RestaurantImagesForm')
    else:
        form = restaurantImagesForm()
    

    return render(request, 'restaurantImageForm.html', {
        'form': form
    })