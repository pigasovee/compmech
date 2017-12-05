# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='#')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('weight', models.IntegerField(default=0, verbose_name='Weight')),
                ('add_to_menu', models.BooleanField(default='False')),
            ],
        ),
    ]
