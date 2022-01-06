from django.shortcuts import render, redirect
#認証機能関連
#from django.contrib.auth.models import user_information
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic import View
from .forms import UserCreateForm
from .forms import LoginForm
from .models import user_information

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
#アカウント作成
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'user'を読み取る
            user = form.cleaned_data.get('user')
            #フォームから'name'を読み取る
            name = form.cleaned_data.get('name')
            #フォームから'mail'を読み取る
            mail = form.cleaned_data.get('mail')
            #フォームから'password'を読み取る
            password = form.cleaned_data.get('password')

            user = authenticate(user=user, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'accounts/create.html', {'form': form,})

create_account = Create_account.as_view()

#ログイン機能
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            user = user_information.objects.get(user=user)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'form': form,})

account_login = Account_login.as_view()