# Generated by Django 3.1.7 on 2021-05-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210522_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previewitem',
            name='videoThumbImg',
            field=models.ImageField(upload_to='productImgs'),
        ),
    ]
