from django.shortcuts import render , redirect
from django.conf import settings
from .models import user_information
from .forms import registrationForm

# Create your views here.

#これは使っていないやつ
def index_template(request):
    return render(request, 'index.html')

#トップページ画面
def TopPage(request):
#セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
#セッションの作成(id)
    if name != 'ゲスト':
        a = user_information.objects.get(user=name)
        request.session['id'] = a.user_id
        
    return render(request, 'TopPage.html' , {
        'name' : name,
    })

#これも使ってないはず
def StoreDetails(request):
    return render(request, 'ShopDetails.html')

#新規登録用フォーム
def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            #ゲストからユーザーname表記へ
            #del request.session['name']
            request.session['name'] = request.POST.getlist('user')
            request.session['id'] = request.POST.getlist('user_id')  
            return redirect('registration')
    else:
        form = registrationForm()
    

    return render(request, 'registration.html', {
        'form': form,
    })
 
def terms(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    return render(request , 'riyou.html' , {
        'name' : name,
    })

def forstores(request):
    #セッション情報があればユーザ―名を無ければゲスト表記
    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'

    return render(request , 'forstores.html' , {
        'name' : name,
    })

def login(request):
    return render(request ,'login.html')