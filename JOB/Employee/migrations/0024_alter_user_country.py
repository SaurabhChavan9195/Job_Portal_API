# Generated by Django 4.1 on 2022-08-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0023_user_country_user_phone_number_user_city_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Country',
            field=models.CharField(default='INDIA', max_length=255),
        ),
    ]
