from django.db import models

# Create your models here.
class store_information(models.Model):
    #restaurant_id = models.IntegerField(primary_key=True)
    #restaurant_name	= models.CharField( "飲食店名" , null = True , max_length = 50)
    #explanation	= models.TextField( "説明文" , max_length = 1000)

    #拾ってきたコード
    #tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    
    #tel = models.CharField("電話番号" , max_length=15)
    #address = models.TextField( "住所" , max_length = 255)

    #郵便番号
    #postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    #postal_code = models.CharField(validators=[postal_code_regex], max_length=7,"郵便番号") 

    #transportation = models.TextField( "アクセス" , max_length = 100)
    #time = models.TextField( "営業時間" , max_length = 100)
    #budget = models.TextField( "予算" , max_length = 50)
    #payment	= models.TextField( "支払方法" , max_length = 100)
    #seat = models.CharField( "席" , null = True , max_length = 20)
    #private_room = models.CharField( "席" , null = True , max_length = 20)
    #reserved = models.CharField( "貸切" , null = True , max_length = 20)
    #smoking = models.CharField( "禁煙&喫煙" , null = True , max_length = 20)
    #parking	= models.CharField( "駐車場" , null = True , max_length = 20)
    #equipment = models.TextField( "空間&設備" , max_length = 50)
    #menu = models.TextField( "メニュー" , max_length = 255)
    #cooking = models.TextField( "料理" , max_length = 255)
    #course = models.TextField( "コース" , max_length = 255)
    #use_scene = models.TextField( "利用シーン" , max_length = 255)
    #location = models.TextField( "ロケーション" , max_length = 255)
    #service = models.TextField( "サービス" , max_length = 500)
    #children = models.TextField( "お子様連れ" , max_length = 255)
    #dress_code = models.TextField( "ドレスコード" , max_length = 100)
    #remarks = models.TextField( "備考" , max_length = 1000)
    #restaurant_allergy = models.TextField( "アレルギー" , max_length = 1000)

#def __str__(self):
    #return self.name