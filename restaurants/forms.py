from django import forms
from .models import restaurant_information , menus , images , review , customer_question , customer_answer

#飲食店情報投稿フォーム
class restaurantInformationForm(forms.ModelForm):
    class Meta:
        model = restaurant_information
        fields = (
            'contributor',
            'restaurant_name',
            'explanation',
            'tel',
            'postal_code',
            'address',
            'transportation',
            'time',
            'budget',
            'payment',
            'seat',
            'private_room',
            'reserved',
            'smoking',
            'parking',
            'equipment',
            'menu',
            'cooking',
            'course',
            'use_scene',
            'location',
            'service',
            'children',
            'dress_code',
            'remarks',
            'restaurant_allergy',
            'tags'
            )

#飲食店のメニュー投稿フォーム
class restaurantMenusForm(forms.ModelForm):
    class Meta:
        model = menus
        fields = (
            'store',
            'name',
            'image',
            'allergy',
            'remarks',
            'price'
        )

#画像投稿用フォーム
class restaurantImagesForm(forms.ModelForm):
    class Meta:
        model = images
        fields = (
            'store',
            'image',
            'attribute'
            )
        labels={
            'image' : '画像',
            'attribute' : '属性',
        }

#レビュー投稿用フォーム
class restaurantReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = (
            'store',
            'review',
            'image',
            'evaluation'
        )

#カスタマーQ&A質問投稿用フォーム
class customerQuestionForm(forms.ModelForm):
    class Meta:
        model = customer_question
        fields = (
            'store',
            'question'
        )

#カスタマーQ&A回答投稿用フォーム
class customerAnswerForm(forms.ModelForm):
    class Meta:
        model = customer_answer
        fields = (
            'question',
            'answer'
        )
