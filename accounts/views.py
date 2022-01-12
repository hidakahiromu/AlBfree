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
    if 'id' in request.session:    
        a = {
            'name' : ','.join(request.session['name'])
        }
    else:
        a = {
            'name' : 'ゲスト'
        }
    return render(request, 'TopPage.html' , a)

#これも使ってないはず
def ShopDetails(request):
    return render(request, 'ShopDetails.html')

#新規登録用フォーム
def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            #ゲストからユーザーname表記へ
            request.session['name'] = request.POST.getlist('user') 
            #userIDをセッションに保存
            request.session['id'] = request.POST.getlist('user_id')  
            return redirect('registration')
    else:
        form = registrationForm()
    

    return render(request, 'registration.html', {
        'form': form,
    })
 
def service(request):
    return render(request , 'riyou.html')
