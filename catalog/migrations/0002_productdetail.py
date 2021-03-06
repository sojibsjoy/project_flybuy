# Generated by Django 3.1.7 on 2021-05-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('brandLogo', models.ImageField(upload_to='brandLogos')),
                ('brandLogoAltText', models.CharField(max_length=30)),
                ('subTitle1', models.CharField(max_length=40)),
                ('subTitle2', models.CharField(max_length=40)),
                ('subTitle3', models.CharField(max_length=40)),
                ('sale', models.FloatField(default=0.0)),
                ('isOffer', models.BooleanField(default=False)),
                ('priceThrough', models.FloatField(default=0.0)),
                ('desc', models.TextField()),
                ('osDetail', models.CharField(max_length=200)),
                ('processorDetial', models.CharField(max_length=200)),
                ('processorTechDetial', models.CharField(max_length=200)),
                ('graphicsDetail', models.CharField(max_length=200)),
                ('memoryDetail', models.CharField(max_length=200)),
                ('harddriveDetail', models.CharField(max_length=200)),
                ('wirelessDetail', models.CharField(max_length=200)),
                ('powerSupplyDetail', models.CharField(max_length=200)),
                ('batteryDetail', models.CharField(max_length=200)),
            ],
        ),
    ]
