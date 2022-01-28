# Generated by Django 3.2.9 on 2022-01-18 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_allergy_tags_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='allergy_evaluation',
            field=models.IntegerField(blank=True, default='1', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='アレルギー対応の評価'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='evaluation',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='評価'),
        ),
    ]