# Generated by Django 3.1.7 on 2021-05-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210522_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=20)),
                ('comment', models.TextField()),
            ],
        ),
    ]
