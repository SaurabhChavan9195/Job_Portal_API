# Generated by Django 4.1 on 2022-08-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0014_rename_college_name_education_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Image',
            new_name='Profile_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(default='static/default.png', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='education',
            name='Education',
            field=models.CharField(choices=[('Secondary School Certificate', 'SSC'), ('Higher Secondary School Certificate', 'HSC'), (' Graduation', 'Graduation')], max_length=255),
        ),
    ]
