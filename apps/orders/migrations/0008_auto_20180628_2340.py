# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180628_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Order in process', max_length=50),
        ),
    ]
