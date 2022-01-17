from django.shortcuts import render , redirect
from django.conf import settings
from .models import allergy_tags , restaurant_information , menus , images , review , customer_question , customer_answer
from .forms import restaurantInformationForm , restaurantMenusForm , restaurantImagesForm , restaurantReviewForm , customerQuestionForm , customerAnswerForm

from django.shortcuts import get_object_or_404




# Create your views here.

#飲食店詳細画面
def StoreDetails(request , pk):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
    
    
    #restaurants_db = restaurant_information.objects.get(pk=pk),
    #'user_db': restaurant_information.objects.get(restaurant_id_id=0),
    #'showdetail_restaurants': restaurant_information.objects.get(restaurant_id=0)
    return render(request, 'StoreDetails.html', {
        'name' : name,
        'restaurants_db' : restaurant_information.objects.get(pk=pk),
        'menu_db' : menus.objects.get(store=pk),
    })


def DbStoreDetails(request, id):

    return render(request, 'StoreDetails.html')

#飲食店一覧画面
def RestaurantsList(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
    
    db = restaurant_information.objects.all()

    #検索結果を取得
    aller = request.GET.getlist("aller")
    pref = request.GET.get("pref")
    genre = request.GET.get("genre")
    date = request.GET.get("date")
    price = request.GET.get("price")
    other = request.GET.get("other")
    smoking = request.GET.get("smoking")

    return render(request , 'restaurantsList.html' , {
        'image_db' : images.objects.all(),
        'restaurants_db' : db,
        'name' : name,
        'aller' : aller,
        'pref' : pref,
        'genre' : genre,
        'date' : date,
        'price' : price,
        'smoking' : smoking,
        'other' : other,
    })

#飲食店の情報投稿フォーム
def RestaurantsForm(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    if request.method == 'POST':
        form = restaurantInformationForm(request.POST)
        
        if form.is_valid():
            form.save()
            #request.session['restaurant_id'] = request.POST.getlist('restaurant_id')
            #登録確認画面へ移行
            return redirect('confirmation')

    else:
        form = restaurantInformationForm(initial={'contributor': request.session['id'],})
    

    return render(request, 'restaurantsInformationForm.html', {
        'form': form,
        'name' : name,
    })

#飲食店のメニュー投稿フォーム
def RestaurantMenuForm(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    if request.method == 'POST':
        form = restaurantMenusForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurantFinishi')
    else:
        form = restaurantMenusForm()
    

    return render(request, 'restaurantMenusForm.html', {
        'form': form,
        'name' : name,
    })

#飲食店の画像(飲食店のトップ画像など)投稿フォーム　※後で関数名は変えるかも
def RestaurantImageForm(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    if request.method == 'POST':
        form = restaurantImagesForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('RestaurantMenuForm')
    else:
        form = restaurantImagesForm()
    

    return render(request, 'restaurantImagesForm.html', {
        'form': form,
        'name' : name,
    })

#レビュー投稿用フォーム
def RestaurantReviewForm(request):
#セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

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

#飲食店情報確認画面
def confirmation(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
    
    return render(request , 'confirmation.html',{
        'name' : name,
    })


def restaurantFinishi(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    return render(request , 'restaurantFinishi.html',{
        'name' : name,
    })


def testForm(request):
    if request.method == 'POST':
        form = testsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testForm')
    else:
        form = testsForm()
    

    return render(request, 'test.html', {
        'form': form
    })
