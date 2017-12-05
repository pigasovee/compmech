# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171130_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('content', models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442')),
                ('images', models.ImageField(height_field='300', upload_to=b'', width_field='400')),
                ('files', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='ac_degree',
            field=models.CharField(max_length=100, verbose_name='\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='ac_title',
            field=models.CharField(max_length=100, verbose_name='\u0423\u0447\u0435\u043d\u043e\u0435 \u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='available',
            field=models.BooleanField(default='True', verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='education',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 (\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c)'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StaffCategory', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='training',
            field=models.CharField(max_length=200, verbose_name='\u041f\u043e\u0432\u044b\u0448\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u043b\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='work_spec_start_date',
            field=models.DateField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='work_start_date',
            field=models.DateField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='add_to_menu',
            field=models.BooleanField(default='False', verbose_name='\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u043c\u0435\u043d\u044e'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content',
            field=models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='title',
            field=models.CharField(default='', max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='\u0412\u0435\u0441 \u0432 \u043c\u0435\u043d\u044e'),
        ),
    ]