from django import forms
from .models import store_images


class store_imagesForm(forms.ModelForm):
    class Meta:
        model = store_images
        fields = ('image' , 'attribute')
