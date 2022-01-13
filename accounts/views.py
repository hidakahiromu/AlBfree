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
    #if not 'id' in request.session:
    #    del request.session['id']
    #    #userIDをセッションに保存
    #    request.session['id'] = user_information.objects.get(user=request.session['name']) 

    if 'name' in request.session:
        name = ','.join(request.session['name']),
    else:
        name = 'ゲスト',
        
    return render(request, 'TopPage.html' , {
        'id' :  user_information.objects.all(),
        'name' : name
    })

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
            del request.session['name']
            request.session['name'] = request.POST.getlist('user')  
            return redirect('registration')
    else:
        form = registrationForm()
    

    return render(request, 'registration.html', {
        'form': form,
    })
 
def service(request):
    return render(request , 'riyou.html')
