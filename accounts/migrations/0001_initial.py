# Generated by Django 3.2.2 on 2021-05-08 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeaddress', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('about', models.CharField(max_length=300)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
