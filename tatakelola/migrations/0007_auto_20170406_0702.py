# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0006_auto_20170406_0656'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
