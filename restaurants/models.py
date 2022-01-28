from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator , MaxValueValidator, MinValueValidator # バリデーション関連のライブラリ
from django.core.exceptions import ValidationError  # 上と同じく
from accounts.models import user_information


import uuid


class allergy_tags(models.Model):
    tag = models.CharField('タグ名', max_length=25)
    image = models.ImageField("画像" , upload_to='allergy')

    def __str__(self):
        return self.tag

# Create your models here.
# 飲食店の情報を管理するテーブル


class restaurant_information(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex

    restaurant_id = models.CharField(
        "飲食店ID", primary_key=True, default=get_uuid_no_dash, max_length=33, editable=False, unique=True)  # 主キー
    contributor = models.ForeignKey(
        user_information, on_delete=models.CASCADE)  # 外部キー
    restaurant_name = models.CharField("飲食店名", max_length=50)
    explanation = models.TextField("説明文", max_length=1000)

    # 拾ってきたコード
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message=(
        "Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message=(
        "Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))

    tel = models.CharField("電話番号", validators=[
                           tel_number_regex], max_length=15)
    postal_code = models.CharField(
        "郵便番号", validators=[postal_code_regex], max_length=7)
    address = models.TextField("住所", max_length=100)

    transportation = models.TextField("アクセス", max_length=100)
    time = models.TextField("営業時間", max_length=100)
    budget = models.TextField("予算", max_length=50)
    payment = models.TextField("支払方法", max_length=100)
    # ↑ここまでは必須情報

    # ここからは一応必須かわからないからblankを付けときます
    seat = models.CharField("席", blank=True, max_length=20)
    private_room = models.CharField("個室", blank=True, max_length=20)
    reserved = models.CharField("貸切", blank=True, max_length=20)
    smoking = models.CharField("禁煙&喫煙", blank=True, max_length=20)
    parking = models.CharField("駐車場", blank=True, max_length=20)
    equipment = models.TextField("空間&設備", blank=True, max_length=50)
    menu = models.TextField("メニュー", blank=True, max_length=255)
    cooking = models.TextField("料理", blank=True, max_length=255)
    course = models.TextField("コース", blank=True, max_length=255)
    use_scene = models.TextField("利用シーン", blank=True, max_length=255)
    location = models.TextField("ロケーション", blank=True, max_length=255)
    service = models.TextField("サービス", blank=True, max_length=500)
    children = models.TextField("お子様連れ", blank=True, max_length=255)
    dress_code = models.TextField("ドレスコード", blank=True, max_length=100)
    remarks = models.TextField("備考", blank=True, max_length=1000)
    support_allergy = models.BooleanField("対応可能店", blank=True)
    allergy_tag = models.ManyToManyField(allergy_tags, blank=False)
    restaurant_allergy = models.TextField("アレルギー", blank=True, max_length=1000)
    tags = models.TextField("タグ", blank=True, max_length=500)

    def __str__(self):
        return self.restaurant_name

# 飲食店のメニューに関するテーブル


class menus(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex

    menu_id = models.CharField("メニューID", primary_key=True, default=get_uuid_no_dash,
                               max_length=33, editable=False, unique=True)  # 主キー
    store = models.ForeignKey(restaurant_information,
                              on_delete=models.CASCADE)  # 外部キー
    name = models.CharField("メニュー名", max_length=50)
    image = models.ImageField("画像", upload_to='menu')
    allergy_tag = models.ManyToManyField(allergy_tags, blank=False)
    remarks = models.TextField("備考", blank=True, max_length=300)
    price = models.IntegerField("値段")

    def __str__(self):
        return self.name

# 飲食店の画像に関するテーブル


class images(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex

    ATTRIBUTE = (
        ('exterior', 'お店の外観'),
        ('introspection', 'お店の内観'),
        ('seat', '席'),
        ('Kitchen', '調理場'),
        ('cooking', '料理'),
        ('others', 'その他'),
    )

    image_id = models.CharField("画像ID", primary_key=True, default=get_uuid_no_dash,
                                max_length=33, editable=False, unique=True)  # 主キー
    store = models.ForeignKey(restaurant_information,
                              on_delete=models.CASCADE)  # 外部キー
    image = models.ImageField("画像", upload_to='images')
    attribute = models.CharField("属性", choices=ATTRIBUTE, max_length=20)

    def __str__(self):
        return self.attribute

# 飲食店のレビュー（評価）に関するテーブル


class review(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex

    review_id = models.CharField("レビューID" ,primary_key=True , default=get_uuid_no_dash, max_length=33, editable=False, unique=True)         #主キー
    store = models.ForeignKey(restaurant_information , on_delete=models.CASCADE)      #外部キー
    user = models.ForeignKey(user_information , on_delete=models.CASCADE)       #外部キー
    title = models.CharField("タイトル" , max_length = 100)
    review = models.TextField( "レビュー" , blank=True , max_length = 500)
    image = models.ImageField("画像" , upload_to='review')

    evaluation = models.IntegerField("評価" , blank=True , validators=[MinValueValidator(1), MaxValueValidator(5)])
    allergy_evaluation = models.IntegerField("アレルギー対応の評価" , blank=True , validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title


# カスタマーQ&Aの質問管理テーブル
class customer_question(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex

    question_id = models.CharField("質問ID" , primary_key=True , default=get_uuid_no_dash, max_length=33, editable=False, unique=True)         #主キー
    store = models.ForeignKey(restaurant_information , on_delete=models.CASCADE)      #外部キー
    user = models.ForeignKey(user_information , on_delete=models.CASCADE)       #外部キー
    question = models.TextField( "質問" , blank=True , max_length = 400)


    def __str__(self):
        return self.question


# カスタマーQ&Aの回答管理テーブル
class customer_answer(models.Model):
    def get_uuid_no_dash():
        return uuid.uuid4().hex
      
      
    answer_id = models.CharField("回答ID" , primary_key=True , default=get_uuid_no_dash, max_length=33, editable=False, unique=True)         #主キー
    question = models.ForeignKey(customer_question , on_delete=models.CASCADE)      #外部キー
    user = models.ForeignKey(user_information , on_delete=models.CASCADE)       #外部キー
    answer = models.TextField( "回答" , blank=True , max_length = 400)


    def __str__(self):
        return self.title
