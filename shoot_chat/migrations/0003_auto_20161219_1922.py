# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_chat', '0002_auto_20161219_1917'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chats',
            new_name='Chat',
        ),
    ]
