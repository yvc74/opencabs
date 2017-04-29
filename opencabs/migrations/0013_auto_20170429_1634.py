# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0012_booking_revenue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('opencabs.booking',),
        ),
        migrations.AddField(
            model_name='booking',
            name='last_payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
