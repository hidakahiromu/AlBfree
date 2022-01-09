from django import forms
from .models import user_information


class registrationForm(forms.ModelForm):
    class Meta:
        model = user_information
        fields = ('user' , 'name' , 'kana' , 'address' , 'password' , 'mail' , 'gender' , 'phone_number')
