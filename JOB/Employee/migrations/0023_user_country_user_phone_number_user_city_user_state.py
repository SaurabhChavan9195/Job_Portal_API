# Generated by Django 4.1 on 2022-08-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0022_alter_profile_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Country',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Phone_number',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
