# Generated by Django 5.0.3 on 2024-04-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='IsActive',
            field=models.BooleanField(default=True),
        ),
    ]
