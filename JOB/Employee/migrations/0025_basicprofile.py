# Generated by Django 4.1 on 2022-08-28 14:46

import Employee.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0024_alter_user_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basicprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=255, verbose_name=Employee.models.User)),
                ('b_location', models.CharField(max_length=255, verbose_name=Employee.models.Experience)),
                ('b_experiance', models.IntegerField(verbose_name=Employee.models.Experience)),
                ('b_CTC', models.IntegerField(verbose_name=Employee.models.Experience)),
                ('b_phone', models.IntegerField(verbose_name=Employee.models.User)),
                ('b_email', models.EmailField(max_length=254, verbose_name=Employee.models.User)),
                ('b_notice_period', models.IntegerField(verbose_name=Employee.models.Experience)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
