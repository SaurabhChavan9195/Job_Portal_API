# Generated by Django 4.1 on 2022-08-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0021_alter_profile_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
    ]