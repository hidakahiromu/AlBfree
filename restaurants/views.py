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
    aller = request.GET.getlist("aller")                #アレルギー  
    pref = request.GET.get("pref")                      #県
    genre = request.GET.get("genre")                    #食ジャンル
    date = request.GET.get("date")                      #日付
    price = request.GET.get("price")                    #料金
    smoking = request.GET.get("smoking")                #禁煙
    reserved = request.GET.get("reserved")              #貸切
    support_allergy = request.GET.get("support_allergy")#アレルギー対応
    equipment = request.GET.get("equipment")            #車いす
    private_room = request.GET.get("private_room")      #個室
    parking = request.GET.get("parking")                #駐車場

    serch_list = restaurant_information.objects.none()    #除外リストの空のクエリを作成
    serch_result = restaurant_information.objects.none()    #表示リストの空のクエリを作成

    if 'たまご' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='1')
    if '牛乳' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='2')
    if '小麦' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='3')
    if 'えび' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='4')
    if 'かに' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='5')
    if '落花生' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='6')
    if 'そば' in aller:
        serch_list = serch_list | restaurant_information.objects.filter(allergy_tag='7')
    if pref != None :
        serch_list = serch_list | restaurant_information.objects.exclude(address__icontains = pref)
    if '全席禁煙' == smoking:
        serch_list = serch_list | restaurant_information.objects.exclude(smoking = '全席禁煙')
    if '貸切あり' == reserved:
        serch_list = serch_list | restaurant_information.objects.exclude(reserved = '貸切あり')
    if 'アレルギー対応可' == support_allergy:
        serch_list = serch_list | restaurant_information.objects.exclude(support_allergy = 'アレルギー対応可')
    if '車いす入店可' == equipment:
        serch_list = serch_list | restaurant_information.objects.exclude(equipment = '車いす入店可')
    if '個室あり' == private_room:
        serch_list = serch_list | restaurant_information.objects.exclude(private_room = '個室あり')
    if '駐車場あり' == parking:
        serch_list = serch_list | restaurant_information.objects.exclude(parking = '駐車場あり')

    for n in db:
        flg = 0
        for i in serch_list:
            if n.restaurant_id == i.restaurant_id:
                flg = 1
        if flg == 0:
            serch_result = serch_result | restaurant_information.objects.filter(restaurant_id = n.restaurant_id)



    return render(request , 'restaurantsList.html' , {
        'image_db' : images.objects.all(),
        'restaurants_db' : db,
        'serch_list' : serch_list,
        'serch_result' : serch_result,
        'name' : name,
        'aller' : aller,
        'pref' : pref,
        'genre' : genre,
        'date' : date,
        'price' : price,
        'smoking' : smoking,
        'reserved' : reserved,
        'support_allergy' : support_allergy,
        'equipment' : equipment,
        'private_room' : private_room,
        'parking' : parking,
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
