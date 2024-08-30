# Generated by Django 5.1 on 2024-08-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additions', '0011_remove_addition_category_addition_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addition',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='addition',
            name='categories',
            field=models.CharField(blank=True, choices=[('education', 'Освіта'), ('leisure', 'Дозвілля'), ('entertainment', 'Розваги'), ('other', 'Інше')], max_length=255, verbose_name='Категорії'),
        ),
    ]
