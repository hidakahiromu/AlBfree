# Generated by Django 3.2.9 on 2022-01-12 00:57


import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_information',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ユーザーID')),
                ('user', models.CharField(max_length=20, verbose_name='ニックネーム')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('kana', models.CharField(max_length=40, verbose_name='フリガナ')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('mail', models.CharField(max_length=50, verbose_name='メールアドレス')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号')),
                ('gender', models.CharField(choices=[('man', '男性'), ('woman', '女性')], max_length=5, verbose_name='性別')),
                ('password', models.CharField(max_length=32, verbose_name='パスワード')),
            ],
        ),
    ]
