# Generated by Django 3.1.7 on 2021-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_productdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
    ]
