# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171130_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to=b''),
        ),
    ]
