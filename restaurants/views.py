from django.shortcuts import render

# Create your views here.
def ShopDetails(request):
    return render(request, 'ShopDetails.html')