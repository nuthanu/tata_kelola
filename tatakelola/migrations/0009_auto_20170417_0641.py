# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0008_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='kebijakan',
            name='nama_perwal',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kebijakan',
            name='no_perwal',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
