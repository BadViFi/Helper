# Generated by Django 5.1 on 2024-08-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_marker_content_marker_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
    ]
