# Generated by Django 4.1.4 on 2022-12-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='img',
            field=models.ImageField(upload_to='pics1'),
        ),
    ]
