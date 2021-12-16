from django.shortcuts import render

# Create your views here.


def index_template(request):
    return render(request, 'index.html')


def TopPage(request):
    return render(request, 'TopPage.html')


def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def service(request):
    return render(request , 'riyou.html')
