# Generated by Django 3.2.9 on 2022-01-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_information',
            name='allergy_tag',
            field=models.ManyToManyField(blank=True, to='restaurants.allergy_tags'),
        ),
    ]
