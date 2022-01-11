from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator  #バリデーション関連のライブラリ
from django.core.exceptions import ValidationError                     #上と同じく

import uuid

# Create your models here.
class user_information(models.Model):

    GENDER = (
        ('man' , '男性'),
        ('woman' , '女性'),
    )

    user_id = models.UUIDField("ユーザーID" , primary_key=True , default=uuid.uuid4 , editable=False)
    user = models.CharField("ニックネーム" , null = False , max_length = 20)
    name = models.CharField("名前" , null = False , max_length = 20)
    kana = models.CharField("フリガナ" , null = False , max_length = 40)
    address = models.CharField("住所" , null = False , max_length = 100)
    mail = models.CharField("メールアドレス" , null = False , max_length = 50)

    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    phone_number = models.CharField("電話番号" , validators=[phone_number_regex] , max_length=15)

    gender = models.CharField("性別" , null = False , choices=GENDER , max_length = 5)
    password = models.CharField("パスワード" , null = False , max_length = 32)

    def __str__(self):
        return self.name