# Generated by Django 3.1.7 on 2021-05-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPhotoArticle', models.BooleanField(default=False)),
                ('isVideoArticle', models.BooleanField(default=False)),
                ('isReviewArticle', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='newArticles')),
                ('imgTitle', models.CharField(max_length=30)),
                ('imgAltText', models.CharField(max_length=30)),
                ('headline', models.CharField(max_length=75)),
                ('date', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
    ]
