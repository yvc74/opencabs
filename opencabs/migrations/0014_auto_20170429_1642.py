# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0013_auto_20170429_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='paid_to_driver',
            new_name='driver_paid',
        ),
        migrations.AddField(
            model_name='booking',
            name='driver_pay',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]