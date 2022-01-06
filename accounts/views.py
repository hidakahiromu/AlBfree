from django.shortcuts import render , redirect
from django.conf import settings
from .models import user_information
from .forms import user_informationForm

# Create your views here.


def index_template(request):
    return render(request, 'index.html')


def TopPage(request):
    return render(request, 'TopPage.html')


def ShopDetails(request):
    return render(request, 'ShopDetails.html')

def registration(request):
    if request.method == 'POST':
        form = registrationForm()
        if form.is_valid():
            form.save()
            return redirect('registration')
    else:
        form = registrationForm()
    

    return render(request, 'registration.html', {
        'form': form
    })
