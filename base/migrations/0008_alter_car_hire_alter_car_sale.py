# Generated by Django 4.1.5 on 2023-01-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_car_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='hire',
            field=models.BooleanField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='sale',
            field=models.BooleanField(max_length=50),
        ),
    ]
