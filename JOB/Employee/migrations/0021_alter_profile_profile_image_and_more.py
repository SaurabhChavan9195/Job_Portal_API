# Generated by Django 4.1 on 2022-08-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0020_remove_resume_resume_id_resume_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_image',
            field=models.ImageField(default='media/default.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(default='media/default.png', upload_to='media/'),
        ),
    ]