from django.contrib import admin

from .models import Addition, Comment

# Register your models here.
admin.site.register(Addition) # Це потрібно для відображення моделі в адмінці

admin.site.register(Comment) # Це потрібно для відображення моделі в адмінці