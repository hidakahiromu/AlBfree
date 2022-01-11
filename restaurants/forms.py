from django import forms
from .models import store_images

#画像投稿用フォーム
class store_imagesForm(forms.ModelForm):
    class Meta:
        model = store_images
        fields = ('store' , 'image' , 'attribute')
        labels={
            'image' : '画像',
            'attribute' : '属性',
        }
