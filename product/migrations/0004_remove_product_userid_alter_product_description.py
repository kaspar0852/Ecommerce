# Generated by Django 5.0.3 on 2024-04-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productreview_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='UserId',
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(max_length=5000),
        ),
    ]
