# Generated by Django 3.1.7 on 2021-05-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='img',
            field=models.ImageField(upload_to='productImgs'),
        ),
    ]