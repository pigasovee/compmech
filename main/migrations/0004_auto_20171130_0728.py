# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171130_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffcategory',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
