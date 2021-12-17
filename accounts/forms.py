from django.contrib.auth.forms import AuthenticationForm 


class LoginForm(AuthenticationForm):    #ログインフォーム
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'    #全てのフォームの部品のclass属性に「form-control」を指定（bootstrapのフォームデザインを利用するため）

            field.widget.attrs['placeholder'] = field.label #全てのフォームの部品にpaceholderを定義して、入力フォームにフォーム名が表示されるように指定。
