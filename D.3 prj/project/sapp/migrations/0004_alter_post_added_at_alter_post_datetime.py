# Generated by Django 5.0.4 on 2024-06-10 12:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0003_remove_post_rating_pos_post_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='added_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
