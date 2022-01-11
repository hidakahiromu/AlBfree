from django import forms
from .models import user_information

#新規登録フォーム
class registrationForm(forms.ModelForm):
    class Meta:
        model = user_information
        fields = ('user' , 'name' , 'kana' , 'address' , 'mail' , 'phone_number' , 'gender',  'password')
