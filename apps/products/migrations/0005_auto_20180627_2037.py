# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180627_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.TextField(),
        ),
    ]
