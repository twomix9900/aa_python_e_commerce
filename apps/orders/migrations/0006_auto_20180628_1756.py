# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180628_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cc_exp_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cc_exp_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cc_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cc_security_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_zip',
            field=models.IntegerField(null=True),
        ),
    ]