# Generated by Django 3.2.15 on 2022-08-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0032_alter_user_country_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone_number',
            field=models.CharField(default=None, max_length=13),
        ),
    ]
