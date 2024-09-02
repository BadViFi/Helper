from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = RichTextField(verbose_name='Біографія', max_length=200, blank=True)
    location = models.CharField(verbose_name='Місце проживання', max_length=255, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=15, blank=True)
    profession = models.CharField(verbose_name='Професія', max_length=30, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'