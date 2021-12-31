from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator  #バリデーション関連のライブラリ
from django.core.exceptions import ValidationError                     #上と同じく
from accounts.models import user_information



# Create your models here.
class store_information(models.Model):
    restaurant_id = models.ForeignKey(user_information , on_delete=models.CASCADE)
    restaurant_name	= models.CharField( "飲食店名" , max_length = 50)
    explanation	= models.TextField( "説明文" , max_length = 1000)

    #拾ってきたコード
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))


    tel = models.CharField("電話番号" , validators=[tel_number_regex] , max_length=15)
    postal_code = models.CharField("郵便番号" , validators=[postal_code_regex], max_length=7) 
    address = models.TextField("住所" , max_length = 100)
    
    transportation = models.TextField( "アクセス" , max_length = 100)
    time = models.TextField( "営業時間" , max_length = 100)
    budget = models.TextField( "予算" , max_length = 50)
    payment	= models.TextField( "支払方法" , max_length = 100)
    #↑ここまでは必須情報

    #ここからは一応必須かわからないからblankを付けときます
    seat = models.CharField( "席" , blank=True , max_length = 20)
    private_room = models.CharField( "個室" , blank=True , max_length = 20)
    reserved = models.CharField( "貸切" , blank=True , max_length = 20)
    smoking = models.CharField( "禁煙&喫煙" , blank=True , max_length = 20)
    parking	= models.CharField( "駐車場" , blank=True , max_length = 20)
    equipment = models.TextField( "空間&設備" , blank=True , max_length = 50)
    menu = models.TextField( "メニュー" , blank=True , max_length = 255)
    cooking = models.TextField( "料理" , blank=True , max_length = 255)
    course = models.TextField( "コース" , blank=True , max_length = 255)
    use_scene = models.TextField( "利用シーン" , blank=True , max_length = 255)
    location = models.TextField( "ロケーション" , blank=True , max_length = 255)
    service = models.TextField( "サービス" , blank=True , max_length = 500)
    children = models.TextField( "お子様連れ" , blank=True , max_length = 255)
    dress_code = models.TextField( "ドレスコード" , blank=True , max_length = 100)
    remarks = models.TextField( "備考" , blank=True , max_length = 1000)
    restaurant_allergy = models.TextField( "アレルギー" , blank=True , max_length = 1000)
    tags = models.TextField("タグ" , blank=True , max_length = 500)

    def __str__(self):
        return self.name

class store_menu(models.Model):
    store = models.ForeignKey(store_information , on_delete=models.CASCADE)
    name = models.CharField( "メニュー名" , max_length = 50)
    allergy = models.CharField( "アレルギー" , blank = True , max_length = 100)
    remarks = models.TextField( "備考" , blank = True , max_length = 300)
    price = models.IntegerField("値段" )

    def __str__(self):
        return self.name


class store_images(models.Model):
    #store = models.ForeignKey(store_information , on_delete=models.CASCADE , blank = True)
    image = models.ImageField(upload_to='images')
    attribute = models.CharField("属性" , max_length = 20)

    def __str__(self):
        return self.name