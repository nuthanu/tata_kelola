# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0009_auto_20170417_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyek',
            name='status',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
    ]
