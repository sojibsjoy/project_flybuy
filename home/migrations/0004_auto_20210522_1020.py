# Generated by Django 3.1.7 on 2021-05-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_newarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarticle',
            name='img',
            field=models.ImageField(upload_to='blogItemPics'),
        ),
    ]