# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20171204_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='\u0412\u0435\u0441'),
        ),
    ]
