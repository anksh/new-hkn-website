# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electeeManagement', '0002_auto_20170219_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_hours',
            name='approved',
            field=models.IntegerField(choices=[(0, 'Unapproved'), (1, 'Approved'), (2, 'Rejected')], default=0),
        ),
    ]
