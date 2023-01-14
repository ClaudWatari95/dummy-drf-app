# Generated by Django 4.1.5 on 2023-01-14 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_car_count_remove_car_created_remove_car_hire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='hire',
            field=models.BooleanField(default='f', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='registration_number',
            field=models.CharField(default='0', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='sale',
            field=models.BooleanField(default='f', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='user_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
