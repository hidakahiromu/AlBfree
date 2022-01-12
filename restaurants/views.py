from django.shortcuts import render , redirect
from django.conf import settings
from .models import restaurant_information , menus , images , review , customer_question , customer_answer
from .forms import restaurantInformationForm , restaurantMenusForm , restaurantImagesForm , restaurantReviewForm , customerQuestionForm , customerAnswerForm



# Create your views here.

#飲食店詳細画面
def StoreDetails(request):
    return render(request, 'StoreDetails.html')

#飲食店一覧画面
def RestaurantsList(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
    
    db = restaurant_information.objects.all()
    return render(request , 'restaurantsList.html' , {
        'restaurants_db' : db,
        'name' : name
    })

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
    

    return render(request, 'restaurantImagesForm.html', {
        'form': form
    })

#レビュー投稿用フォーム
def RestaurantReviewForm(request):
    if request.method == 'POST':
        form = restaurantReviewForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('RestaurantReviewForm')
    else:
        form = restaurantReviewForm()
    

    return render(request, 'restaurantReviewForm.html', {
        'form': form
    })

#カスタマーQ&A質問投稿用フォーム
def CustomerQuestionForm(request):
    if request.method == 'POST':
        form = customerQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CustomerQuestionForm')
    else:
        form = customerQuestionForm()
    

    return render(request, 'customerQuestionForm.html', {
        'form': form
    })


#カスタマーQ&A回答投稿用フォーム
def CustomerAnswerForm(request):
    if request.method == 'POST':
        form = customerAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CustomerAnswerForm')
    else:
        form = customerAnswerForm()
    

    return render(request, 'customerAnswerForm.html', {
        'form': form
    })