from django.shortcuts import render
#認証機能関連
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm    # forms.pyで定義したユーザ認証画面用フォームをImport

# Create your views here.


def index_template(request):
    return render(request, 'index.html')


def TopPage(request):
    return render(request, 'TopPage.html')


def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def service(request):
    return render(request , 'riyou.html')

#認証機能関連

class Login(LoginView):
    #ログインページ
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    #ログアウトページ
    template_name = 'login.html'
#複数のクラスを承継する場合はLoginRequiredMixinを一番最初に指定するように