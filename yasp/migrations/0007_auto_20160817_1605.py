# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-17 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yasp', '0006_auto_20160817_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yasp.Menu', verbose_name='menu'),
        ),
    ]