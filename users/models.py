from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='media/images/default_image_profile.jpg')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username








