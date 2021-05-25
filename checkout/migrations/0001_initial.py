# Generated by Django 3.1.7 on 2021-05-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTotal', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('delivery', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
            ],
        ),
    ]
