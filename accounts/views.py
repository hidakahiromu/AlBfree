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
    #a = user_information.objects.filter(user="aaaa")
    #if not 'id' in request.session:
    #    del request.session['id']
    #    #userIDをセッションに保存
    #    request.session['id'] = user_information.objects.values_list('user_id', flat=True).get(user=['aaaa'])
    #    a = request.session['id']

    if 'name' in request.session:
        name = ','.join(request.session['name'])
    else:
        name = 'ゲスト'
        
    return render(request, 'TopPage.html' , {
        'name' : name,
        'id' : a,
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
            del request.session['name']
            request.session['name'] = request.POST.getlist('user')
            request.session['id'] = request.POST.getlist('user_id')  
            return redirect('registration')
    else:
        form = registrationForm()
    

    return render(request, 'registration.html', {
        'form': form,
    })
 
def terms(request):
    return render(request , 'riyou.html')

def forstores(request):
    return render(request , 'forstores.html')

def login(request):
    return render(request ,'login.html')