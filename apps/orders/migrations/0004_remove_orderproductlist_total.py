# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180628_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproductlist',
            name='total',
        ),
    ]