# Generated by Django 3.2.2 on 2021-05-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210508_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_demo.png', null=True, upload_to=''),
        ),
    ]
