# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_menuitem_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='url',
            field=models.CharField(default='', max_length=256, verbose_name='URL'),
        ),
    ]
