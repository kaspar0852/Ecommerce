# Generated by Django 5.0.3 on 2024-04-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_user_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='OrderNumber',
            field=models.IntegerField(default=0),
        ),
    ]
