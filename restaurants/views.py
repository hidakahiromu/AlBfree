from django.shortcuts import render , redirect
from django.conf import settings
from .forms import store_imagesForm
from .models import store_information , store_images , store_menu


# Create your views here.

#飲食店詳細画面
def StoreDetails(request):
    return render(request, 'StoreDetails.html')

#飲食店一覧画面
def RestaurantsList(request):
    db = {
        'restaurants_db' : store_information.objects.all(),
        #'user_db' : store_information.objects.get(contributor = 0),
    }
    return render(request , 'restaurantsList.html' , db)


#飲食店の画像(飲食店のトップ画像など)投稿フォーム　※後で関数名は変えるかも
def Form(request):
    if request.method == 'POST':
        form = store_imagesForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Form')
    else:
        form = store_imagesForm()
    

    return render(request, 'modelForm.html', {
        'form': form
    })