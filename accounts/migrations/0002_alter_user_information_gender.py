# Generated by Django 3.2.9 on 2022-01-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='gender',
            field=models.CharField(choices=[('man', '男性'), ('woman', '女性')], max_length=5, verbose_name='性別'),
        ),
    ]
