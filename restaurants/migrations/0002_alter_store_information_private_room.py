# Generated by Django 3.2.9 on 2021-12-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_information',
            name='private_room',
            field=models.CharField(blank=True, max_length=20, verbose_name='個室'),
        ),
    ]
