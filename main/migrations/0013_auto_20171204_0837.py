# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20171204_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='weight',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent_item',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='main.MenuItem', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442'),
        ),
    ]
