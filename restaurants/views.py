from django.shortcuts import render , redirect
from django.conf import settings
from .forms import store_imagesForm
from .models import store_information , store_images , store_menu


# Create your views here.


def StoreDetails(request):
    return render(request, 'StoreDetails.html')


def RestaurantsList(request):
    db = {
        'restaurants_db' : store_information.objects.all(),
        'user_db' : store_information.objects.get(restaurant_id = 0),
        'auth' : store_menu.objects.get(store_id = 1),
        'img' : store_images.objects.get(attribute = "neko"),
    }
    return render(request , 'restaurantsList.html' , db)

def Form(request):
    if request.method == 'POST':
        form = store_imagesForm(request.POST , request.FILES , request.POST)
        if form.is_valid():
            form.save()
            return redirect('Form')
    else:
        form = store_imagesForm()
    

    return render(request, 'modelForm.html', {
        'form': form
    })