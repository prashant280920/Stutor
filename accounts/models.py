from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    homeaddress = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    specialization = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    about = models.CharField(max_length=300, null=True, blank=True)
    profile_pic = models.ImageField(
        default='profile_demo.png', null=True, blank=True)

    # def save(self):
    #     super().save()
    #     img = profile_pic.open(self.profile_pic.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)

    def __str__(self):
        return self.user.username
