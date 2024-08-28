from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Addition(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Освіта'),
        ('leisure', 'Дозвілля'),
        ('entertainment', 'Розваги'),
        ('other', 'Інше'),
    ]
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Автор', related_name = 'posts',  null=True, default=None)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Малюнок', upload_to='media/post_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    is_published = models.BooleanField(verbose_name='Опубліковано', default=False, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    
    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_published}'
    
    class Meta: 
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'
        ordering = ['-created_at']
        
        
class Comment(models.Model):
    detale = models.ForeignKey(Addition, on_delete=models.CASCADE, verbose_name='Допис', related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Автор', related_name = 'comments',  null=True, default=None)
    content = models.TextField(verbose_name='Контент')
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    
    def __str__(self):
        return f'{self.author} - {self.created_at}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']
        
        
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач', related_name = 'favorites')
    addition = models.ForeignKey(Addition, on_delete=models.CASCADE, verbose_name='Допис')

    def __str__(self):
        return f'{self.addition.title} - {self.user.username}'

    class Meta:
        verbose_name = 'Обране'
        verbose_name_plural = 'Обране'
        unique_together = ('user', 'addition')