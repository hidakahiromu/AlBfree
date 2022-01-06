from .models import user_information
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 


class UserCreateForm(UserCreationForm): #アカウント作成フォーム
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['mail'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):    #ログインフォーム
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['mail'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class Meta:
    model = user_information
    fields = ("user", "name", "mail", "password",)