# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-25 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='poster',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
