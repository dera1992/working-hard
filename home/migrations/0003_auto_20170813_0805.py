# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='User',
            new_name='user',
        ),
    ]
