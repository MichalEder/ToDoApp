# Generated by Django 2.2 on 2024-02-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp_api', '0003_auto_20240204_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]